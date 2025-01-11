import time
from ._mk import Mouse, Keyboard
from ._color import ColorDetector

class Automation:
    def __init__(self, config, sm, tm, wm):
        self.sm = sm
        self.tm = tm
        self.wm = wm
        self.config = config
        self.mouse = Mouse()
        self.keyboard = Keyboard()
        self.color_detector = ColorDetector(wm)

    def rel(self, x, y):
        """set coordinates relative to the target window"""
        rect = self.wm.get_rect()
        if rect:
            screen_x = rect['left'] + x
            screen_y = rect['top'] + y
        return screen_x, screen_y

    # RED LIGHT!.... GREEEEEEEN LIIIIIIIGGHHHTTT
    def red_light_green_light(self):

        # text coords (they overlap so we just focus a single point)
        TEXT_X = 396
        TEXT_Y = 128

        # text colors
        GREEN = (83, 255, 56)
        RED = (255, 24, 24)

        # key to press
        MOVE_KEY = 'a'

        self.sm.update('status_text', 'starting')

        try:
            while self.config.RUNNING:

                # get current color of text
                current_color = self.color_detector.get_pixel(TEXT_X, TEXT_Y)
                if current_color is None:
                    continue

                # green light
                if self.color_detector.check(TEXT_X, TEXT_Y, GREEN, tolerance=50):
                    self.sm.update('status_text', 'moving')
                    self.keyboard.press(MOVE_KEY)

                    # move until color changes
                    while (self.config.RUNNING and self.color_detector.check(TEXT_X, TEXT_Y, GREEN, tolerance=30)):
                        time.sleep(0.1)

                    # stop when color changes
                    self.keyboard.release(MOVE_KEY)
                    self.sm.update('status_text', 'stopped')

                # red light
                elif self.color_detector.check(TEXT_X, TEXT_Y, RED, tolerance=30):
                    self.sm.update('status_text', 'waiting')
                    self.keyboard.release(MOVE_KEY)
                    # wait for green
                    while (self.config.RUNNING and 
                           self.color_detector.check(TEXT_X, TEXT_Y, RED, tolerance=30)):
                        time.sleep(0.1)

                time.sleep(0.1)

        # release key if error
        except Exception as e:
            print(e)
            self.keyboard.release(MOVE_KEY)
        finally:
            self.keyboard.release(MOVE_KEY)
            self.sm.update('status_text', 'oh shi')

    def start(self):
        if not self.config.RUNNING:
            self.config.RUNNING = True
            if not self.wm.wait_target_win():
                self.sm.update('failed', 'could not find target window')
                self.config.RUNNING = False
                return
            self.sm.configure('run_button', label='STOP')
            self.tm.add_thread('red_light_green_light', self.red_light_green_light)
        else:
            self.stop()

    def stop(self):
        self.config.RUNNING = False
        self.tm.stop_all_threads()
        self.sm.configure('run_button', label='START')
