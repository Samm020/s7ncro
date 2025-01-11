import dearpygui.dearpygui as dpg
from threading import Lock

class StatusManager:
    def __init__(self):
        self.status_lock = Lock()

    def update(self, target, value):
        """update the status text thing yeah"""
        with self.status_lock:
            if dpg.is_dearpygui_running():
                dpg.set_value(target, value)

    def configure(self, target, **kwargs):
        """configure dpg thing"""
        with self.status_lock:
            if dpg.is_dearpygui_running():
                dpg.configure_item(target, **kwargs)
