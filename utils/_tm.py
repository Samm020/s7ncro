import threading

class ThreadManager:
    def __init__(self):
        self.active_threads = {}
        self.thread_lock = threading.Lock()
        self.stop_event = threading.Event()

    def _wrapped_target(self, name, target, args, kwargs):
        """wrapper for thread target to handle cleanup stuff"""
        try:
            target(*args, **kwargs)
        except Exception as e:
            print(f'thread {name} error: {e}')
        finally:
            with self.thread_lock:
                if name in self.active_threads:
                    del self.active_threads[name]

    def add_thread(self, name, target, *args, **kwargs):
        """
        start new thread with given name and target function

        ---

        args:
            name (_type_): _description_
            target (_type_): _description_
        """
        with self.thread_lock:
            if name in self.active_threads and self.active_threads[name].is_alive():
                return False

            thread = threading.Thread(
                target=self._wrapped_target,
                args=(name, target, args, kwargs),
                daemon=True
            )
            self.active_threads[name] = thread
            thread.start()
            return True

    def stop_thread(self, name):
        """stop a thread"""
        with self.thread_lock:
            if name in self.active_threads:
                self.stop_event.set()
                self.active_threads[name].join(timeout=1.0)
                del self.active_threads[name]
                self.stop_event.clear()

    def stop_all_threads(self):
        """stop all active threads"""
        current_thread = threading.current_thread()
        with self.thread_lock:
            self.stop_event.set()
            for name, thread in list(self.active_threads.items()):
                if thread is current_thread:
                    continue
                thread.join(timeout=1.0)
            self.active_threads.clear()
            self.stop_event.clear()

    def is_thread_running(self, name):
        """check if thread is running"""
        with self.thread_lock:
            return name in self.active_threads and self.active_threads[name].is_alive()
