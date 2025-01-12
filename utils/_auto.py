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
        self.state = 0

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
    
    def release_keys(self):
        """release all keys"""
        self.keyboard.release(self.config.JUMP)
        self.keyboard.release(self.config.LEFT)
        self.keyboard.release(self.config.RIGHT)
        self.keyboard.release(self.config.FORWARD)
        self.keyboard.release(self.config.BACKWARD)

    # check if in lobby
    def _in_lobby(self):
        if self.state == 0 and self.color.region_check([self.config.LOBBY_X, self.config.LOBBY_Y, 2], self.config.LOBBY_COL):
            self.sm.update('status_text', 'in lobby')
            self.release_keys()
            self.keyboard.press(self.config.RIGHT)

            # maybe running into wall makes orientation issue?
            time.sleep(6) 
            self.wm.activate()
            self.moverel(400,300)
            self.mouse.press('r')
            self.moverel(300,300)
            self.mouse.release('r')

            # wait until menu icon is gone
            #while (self.config.RUNNING and self.color.region_check([self.config.LOBBY_X, self.config.LOBBY_Y, 2], self.config.LOBBY_COL)):
            #    time.sleep(0.1)

            # stop moving when done
            self.keyboard.release(self.config.RIGHT)

            # set state to prevent further action
            self.state = 1

    # check the pink game name text
    def _check_game(self):
        if self.color.region_check([self.config.RLGL_GAME_X, self.config.RLGL_GAME_Y, 3], self.config.GAME_COL):
            self.sm.update('status_text', 'rlgl')
            self.keyboard.release(self.config.RIGHT)
            self.keyboard.press(self.config.LEFT)
            self.state = 2
            time.sleep(9)
        elif self.color.region_check([self.config.TEXT_X, self.config.TEXT_Y, 3], self.config.GAME_COL):
            self.sm.update('status_text', 'obby')
            self.keyboard.press(self.config.RIGHT)
            self.keyboard.press(self.config.FORWARD)
            self.state = 3
            time.sleep(9)

    # check for points earned text
    def _check_point(self):
        if self.state == 2 and self.color.region_check([self.config.TEXT_X, self.config.TEXT_Y, 3], self.config.POINT_COL):
            self.release_keys()
            self.sm.update('status_text', 'finished')
            self.moverel(self.config.HOME_X, self.config.HOME_Y)
            self.mouse.click()
            self.state = 0
            time.sleep(9)

    def _check_eliminate(self):
        if self.color.region_check([self.config.ELIM_X, self.config.ELIM_Y, 3], self.config.ELIM_COL):
            self.release_keys()
            self.sm.update('status_text', 'eliminate')
            self.moverel(self.config.ELIM_X-100, self.config.ELIM_Y-10)
            self.mouse.click()
            self.state = 0
            time.sleep(9)

    def rlgl(self):
        # green light
        if self.color.region_check([self.config.RLGL_X, self.config.RLGL_Y, 3], self.config.RLGL_GREEN, tolerance=80):
            self.sm.update('status_text', 'moving')
            self.keyboard.press(self.config.LEFT)

            # move until color changes
            while (self.config.RUNNING and self.color.region_check([self.config.RLGL_X, self.config.RLGL_Y, 3], self.config.RLGL_GREEN, tolerance=80)):
                self._check_point()
                time.sleep(0.1)

        # red light
        elif self.color.region_check([self.config.RLGL_X, self.config.RLGL_Y, 3], self.config.RLGL_RED, tolerance=30):
            self.sm.update('status_text', 'waiting')
            time.sleep(0.2) # move a bit further for free
            self.keyboard.release(self.config.LEFT)

            # wait for green
            while (self.config.RUNNING and self.color.region_check([self.config.RLGL_X, self.config.RLGL_Y, 3], self.config.RLGL_RED, tolerance=30)):
                self._check_point()
                time.sleep(0.1)

    def obby(self):
        pass

    # mini games loop
    def minigames(self):

        # slight delay
        for i in range(3, 0, -1):
            self.sm.update('status_text', f'{i}...')
            time.sleep(1)
        self.wm.activate()

        try:
            while not self.tm.stop_event.is_set() and self.config.RUNNING:

                self._in_lobby()
                self._check_eliminate()
                self._check_game()

                # RED LIGHT.... GREEEEEEEN LIIIIIIIGGHHHTTT
                if self.state == 2:
                    self.rlgl()

                # THE OBBBYYYYYYYYYYY
                #elif self.state == 3:
                #    pass

                self.sm.update('status_text', 'idle')
                time.sleep(0.1)

        # release key if error
        except Exception as e:
            self.release_keys()
            print(e)
        finally:
            self.release_keys()
            self.sm.update('status_text', 'stopped')

    def start(self):
        if not self.config.RUNNING:
            self.config.RUNNING = True
            if not self.wm.wait_target_win():
                self.sm.update('status_text', 'failed')
                self.sm.update('status_text_hover', 'cant find target window, select again')
                self.config.HWND = None
                self.config.RUNNING = False
                return
            self.sm.configure('run_button', label='STOP')
            self.tm.add_thread('minigames', self.minigames)
        else:
            self.stop()

    def stop(self):
        self.release_keys()
        self.config.RUNNING = False
        self.tm.stop_all_threads()
        self.sm.configure('run_button', label='START')
        self.state = 0
