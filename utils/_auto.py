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
        self.color = ColorDetector(wm)

    def rel(self, x, y):
        """set coordinates relative to target window"""
        rect = self.wm.get_rect()
        if rect:
            screen_x = rect['left'] + x
            screen_y = rect['top'] + y
        return screen_x, screen_y

    def moverel(self, x, y):
        """move mouse cursor relative to target window"""
        screen_x, screen_y = self.rel(x,y)
        self.mouse.move(screen_x,screen_y)

    # RED LIGHT!.... GREEEEEEEN LIIIIIIIGGHHHTTT
    def red_light_green_light(self):

        # slight delay
        for i in range(3, 0, -1):
            self.sm.update('status_text', f'{i}...')
            time.sleep(1)
        self.wm.activate()

        # lobby indicator (hoverboard icon)
        LOBBY_X = 420
        LOBBY_Y = 535
        LOBBY = (210, 235, 35)

        # text (they overlap so we just focus a single point)
        TEXT_X = 396
        TEXT_Y = 128
        GREEN = (83, 255, 56)
        RED = (255, 24, 24)

        # the minigame name text (to get as close to start as possible)
        GAME = (253, 48, 145)

        # gained points text (click home after it does)
        POINT_X = 404
        POINT_Y = 426
        POINT = (255, 255, 1)
        HOME_X = 404
        HOME_Y = 516

        # keys
        RIGHT = 'd'
        LEFT = 'a'

        try:
            while not self.tm.stop_event.is_set() and self.config.RUNNING:

                # if hoverboard, move right
                if self.color.check(LOBBY_X, LOBBY_Y, LOBBY):
                    self.sm.update('status_text', 'lobby')
                    self.keyboard.press(RIGHT)

                    # wait until hoverboard icon is gone
                    while (self.config.RUNNING and self.color.check(LOBBY_X, LOBBY_Y, LOBBY)):
                        time.sleep(0.1)

                    # stop moving when done
                    self.keyboard.release(RIGHT)

                # scan for the pink text before the red light green light to get ahead
                if self.color.check(POINT_X, POINT_Y, GAME):
                    self.keyboard.press(LEFT)
                    self.sm.update('status_text', 'line up')
                    time.sleep(6)

                # green light
                if self.color.check(TEXT_X, TEXT_Y, GREEN, tolerance=60):
                    self.sm.update('status_text', 'moving')
                    self.keyboard.press(LEFT)

                    # move until color changes
                    while (self.config.RUNNING and self.color.check(TEXT_X, TEXT_Y, GREEN, tolerance=60)):

                        # scan for points text
                        if self.color.region_check([POINT_X-3, POINT_Y-3, POINT_X+3, POINT_Y+3], POINT):
                            self.sm.update('status_text', 'cleared')
                            self.keyboard.release(LEFT)
                            self.moverel(HOME_X, HOME_Y)
                            self.mouse.click()
                            time.sleep(5)

                        time.sleep(0.1)

                # red light
                elif self.color.check(TEXT_X, TEXT_Y, RED, tolerance=30):
                    self.sm.update('status_text', 'waiting')
                    time.sleep(0.2) # move a bit further for free
                    self.keyboard.release(LEFT)

                    # wait for green
                    while (self.config.RUNNING and self.color.check(TEXT_X, TEXT_Y, RED, tolerance=30)):

                        # scan for points text
                        if self.color.region_check((POINT_X-3, POINT_Y-3, POINT_X+3, POINT_Y+3), POINT):
                            self.sm.update('status_text', 'cleared')
                            self.moverel(HOME_X, HOME_Y)
                            self.mouse.click()
                            time.sleep(5)

                        time.sleep(0.1)

                self.sm.update('status_text', 'idle')
                time.sleep(0.1)

        # release key if error
        except Exception as e:
            print(e)
            self.keyboard.release(RIGHT)
            self.keyboard.release(LEFT)
        finally:
            self.keyboard.release(RIGHT)
            self.keyboard.release(LEFT)
            self.sm.update('status_text', 'stopped')

    def start(self):
        if not self.config.RUNNING:
            self.config.RUNNING = True
            if not self.wm.wait_target_win():
                self.sm.update('status_text', 'failed')
                self.sm.update('status_text_hover', 'could not find target window')
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
