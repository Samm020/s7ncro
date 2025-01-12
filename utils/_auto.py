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

        # text coords
        self.text_x = 404
        self.text_y = 426
        self.point_col = (255, 255, 1)
        self.game_col = (253, 48, 145)

        # lobby indicator (menu icon)
        self.lobby_x = 420
        self.lobby_y = 535
        self.lobby_col = (210, 235, 35)

        # home icon coords
        self.home_x = 404
        self.home_y = 516

        # rlgl colors
        self.rlgl_x = 396
        self.rlgl_y = 128
        self.rlgl_green = (83, 255, 56)
        self.rlgl_red = (255, 24, 24)
        self.rlgl_col = (230, 235, 157)

        # obby color
        self.obby_x = 790
        self.obby_y = 590
        self.obby_col = (83, 154, 195)

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

    # RED LIGHT.... GREEEEEEEN LIIIIIIIGGHHHTTT
    def rlgl(self):

        # slight delay
        for i in range(3, 0, -1):
            self.sm.update('status_text', f'{i}...')
            time.sleep(1)
        self.wm.activate()

        try:
            while not self.tm.stop_event.is_set() and self.config.RUNNING:

                # check menu icon exist
                if self.color.region_check([self.lobby_x, self.lobby_y, 2], self.lobby_col):
                    self.sm.update('status_text', 'in lobby')
                    self.keyboard.release('a')
                    self.keyboard.press('d')

                    # wait until menu icon is gone
                    while (self.config.RUNNING and self.color.region_check([self.lobby_x, self.lobby_y, 2], self.lobby_col)):
                        time.sleep(0.1)

                    # stop moving when done
                    self.keyboard.release('d')

                # scan for the pink text before the red light green light to get ahead
                if self.color.region_check([self.text_x, self.text_y, 3], self.game_col):

                    # check if wrong orientation
                    # soon

                    self.keyboard.release('d')
                    self.keyboard.press('a')
                    self.sm.update('status_text', 'line up')
                    time.sleep(9)

                # green light
                if self.color.region_check([self.rlgl_x, self.rlgl_y, 3], self.rlgl_green, tolerance=80):
                    self.sm.update('status_text', 'moving')
                    self.keyboard.press('a')

                    # move until color changes
                    while (self.config.RUNNING and self.color.region_check([self.rlgl_x, self.rlgl_y, 3], self.rlgl_green, tolerance=80)):

                        # scan for points text
                        if self.color.region_check([self.text_x, self.text_y, 3], self.point_col):
                            self.sm.update('status_text', 'finished')
                            self.keyboard.release('a')
                            self.moverel(self.home_x, self.home_y)
                            self.mouse.click()
                            time.sleep(5)

                        time.sleep(0.1)

                # red light
                elif self.color.region_check([self.rlgl_x, self.rlgl_y, 3], self.rlgl_red, tolerance=30):
                    self.sm.update('status_text', 'waiting')
                    time.sleep(0.2) # move a bit further for free
                    self.keyboard.release('a')

                    # wait for green
                    while (self.config.RUNNING and self.color.region_check([self.rlgl_x, self.rlgl_y, 3], self.rlgl_red, tolerance=30)):

                        # scan for points text
                        if self.color.region_check([self.text_x, self.text_y, 3], self.point_col):
                            self.sm.update('status_text', 'finished')
                            self.moverel(self.home_x, self.home_y)
                            self.mouse.click()
                            time.sleep(5)

                        time.sleep(0.1)

                self.sm.update('status_text', 'idle')
                time.sleep(0.1)

        # release key if error
        except Exception as e:
            print(e)
            self.keyboard.release('d')
            self.keyboard.release('a')
        finally:
            self.keyboard.release('d')
            self.keyboard.release('a')
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
            self.tm.add_thread('rlgl', self.rlgl)
            #self.minigames()
        else:
            self.stop()

    def stop(self):
        self.config.RUNNING = False
        self.tm.stop_all_threads()
        self.sm.configure('run_button', label='START')
