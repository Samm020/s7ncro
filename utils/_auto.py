import time
from ._mk import Mouse, Keyboard
from ._color import Color

def running_check(func):
    def wrapper(self, *args, **kwargs):
        if self.config.RUNNING:
            return func(self, *args, **kwargs)
    return wrapper

class Automation:
    def __init__(self, config, sm, tm, wm):
        self.sm = sm
        self.tm = tm
        self.wm = wm
        self.config = config
        self.mouse = Mouse()
        self.keyboard = Keyboard()
        self.color = Color(wm)
        self.state = 0
        self.orientation = 0

    def rel(self, x, y):
        """set coordinates relative to target window"""
        rect = self.wm.get_rect()
        if rect:
            screen_x = rect['left'] + x
            screen_y = rect['top'] + y
        return screen_x, screen_y

    @running_check
    def moverel(self, x, y):
        """move mouse cursor relative to target window"""
        screen_x, screen_y = self.rel(x, y)
        self.mouse.move(screen_x, screen_y)

    @running_check
    def click(self, btn='l', hold=70):
        self.mouse.click(btn, hold)

    @running_check
    def keydown(self, key):
        self.keyboard.press(key)

    @running_check
    def keyup(self, key):
        self.keyboard.release(key)

    @running_check
    def keypress(self, key):
        self.keyboard.keypress(key)

    def release_keys(self):
        """release all keys"""
        self.keyup(self.config.JUMP)
        self.keyup(self.config.LEFT)
        self.keyup(self.config.RIGHT)
        self.keyup(self.config.FORWARD)
        self.keyup(self.config.BACKWARD)

    def sleep(self, seconds):
        """sleep while checking running state"""
        for _ in range(int(seconds)):
            if not self.config.RUNNING:
                break
            time.sleep(1)

    # set orientation key
    def _orientation_key(self):
        if self.orientation == 0:
            return self.config.LEFT
        elif self.orientation == 1:
            return self.config.RIGHT
        elif self.orientation == 2:
            return self.config.FORWARD
        elif self.orientation == 3:
            return self.config.BACKWARD

    # chekc if disconencted
    def _check_disconnected(self):
        # if white and gray buttons exists, it means its possible to reconnect
        rec1, col1 = [self.config.RECONNECT_POS.x, self.config.RECONNECT_POS.y, 2], self.config.RECONNECT_COL
        rec2, col2 = [self.config.LEAVE_POS.x, self.config.LEAVE_POS.y, 2], self.config.LEAVE_COL
        if self.color.region_check(rec1, col1) and self.color.region_check(rec2, col2):
            self.sm.update('status_text', 'discon..')
            self.moverel(self.config.RECONNECT_POS.x+70, self.config.RECONNECT_POS.y+5)
            self.click()
            self.sleep(10)

    # Check if you are in spawn world
    def _check_spawn_world(self):
        if self.color.check(
            self.config.W1_BLOCK_POS.x,
            self.config.W1_BLOCK_POS.y,
            self.config.W1_BLOCK_COL
        ):
            if self.state != 4:
                self.sm.update('status_text', 'in spawn')
                self.release_keys()
                # click tp
                self.moverel(self.config.TELEPORT_POS.x, self.config.TELEPORT_POS.y)
                self.click()
                self.sleep(1)
                # area 2
                self.moverel(310, 200)
                self.click()
                self.sleep(4)
                # click tp
                self.moverel(self.config.TELEPORT_POS.x, self.config.TELEPORT_POS.y)
                self.click()
                self.sleep(1)
                # spawn
                self.moverel(25, 195)
                self.click()
                self.sleep(4)
                # move right
                self.keydown(self.config.RIGHT)
                self.sleep(2)
                self.keyup(self.config.RIGHT)
                # forward to enter event
                self.keydown(self.config.FORWARD)
                self.sleep(2)
                self.keyup(self.config.FORWARD)
                self.sleep(3)
                # move to enterance distance
                self.keydown(self.config.FORWARD)
                self.sleep(2)
                self.keyup(self.config.FORWARD)
                # move into portal
                self.keydown(self.config.RIGHT)
                self.sleep(2)
                self.keyup(self.config.RIGHT)
                self.keydown(self.config.RIGHT)
                self.keydown(self.config.JUMP)
                self.sleep(3)
                self.release_keys()
                self.state = 4
            return True
        elif self.state == 4:
            self.state = 0
        return False

    # check if in lobby
    def _check_lobby(self):
        if self.state == 0 and self.color.region_check(
            [self.config.LOBBY_POS.x, self.config.LOBBY_POS.y, 2], self.config.LOBBY_COL):
            self.sm.update('status_text', 'in lobby')
            self.release_keys()
            self.sleep(3)
            self.keydown(self.config.RIGHT)
            self.sleep(9)
            self.keyup(self.config.RIGHT)

            # new lobby workaround, just moves in zig zags across the queue zone
            def _zigzag(direction):
                self.keydown(direction)
                for _ in range(3):
                    if self.config.RUNNING:
                        self.keydown(self.config.LEFT)
                        time.sleep(0.4)
                        self.keyup(self.config.LEFT)
                        self.keydown(self.config.RIGHT)
                        time.sleep(0.8)
                        self.keyup(self.config.RIGHT)
                self.keyup(direction)
            _zigzag(self.config.FORWARD)
            _zigzag(self.config.BACKWARD)

            # stop moving when done
            self.keyup(self.config.RIGHT)

            # set state to prevent further action
            self.state = 1

    # check the pink game name text
    def _check_game(self) -> bool:

        # if rlgl
        if self.color.region_check([self.config.RLGL_GAME_POS.x, self.config.RLGL_GAME_POS.y, 3], self.config.GAME_COL):

            # fix orientation for all directions (scans for the position of red start line)
            # big area so if players cover up the line some parts are still visible
            s_left = (self.config.RLGL_ORI_POS_LX, self.config.RLGL_ORI_POS_LY)
            s_right = (self.config.RLGL_ORI_POS_RX, self.config.RLGL_ORI_POS_RY)
            m_left = [self.config.RLGL_ORI_POS_ML.x, self.config.RLGL_ORI_POS_ML.y, 40]
            m_right = [self.config.RLGL_ORI_POS_MR.x, self.config.RLGL_ORI_POS_MR.y, 40]
            color = self.config.RLGL_ORI_COL

            # holy moly checks
            # if macro is still moving to the wrong direction then idk wtf you did wrong
            def check_left():
                return self.color.region_check(s_left, color, 0) or self.color.region_check(m_left, color, 0)
            def check_right():
                return self.color.region_check(s_right, color, 0) or self.color.region_check(m_right, color, 0)
            left = check_left()
            right = check_right()

            # normal left orientation
            if left and not right:
                self.orientation = 0

            # right orientation
            elif not left and right:
                self.orientation = 1

            # forward orientation
            elif left and right:
                self.orientation = 2

            # backwards orientation
            elif not left and not right:
                self.orientation = 3

            # just reset it cant find orientation to avoid losing more boost time
            else:
                self.sm.update('status_text', 'reset')
                self.moverel(self.config.HOME_POS.x, self.config.HOME_POS.y)
                self.click()
                self.state = 0
                self.sleep(5)

            # initial pre move
            self.wm.activate()
            self.sm.update('status_text', 'rlgl')
            self.keydown(self._orientation_key())
            self.state = 2
            self.sleep(9)
            return True

        # if obby
        elif self.color.region_check(
            [self.config.TEXT_POS.x, self.config.TEXT_POS.y, 3], self.config.GAME_COL):
            self.wm.activate()
            self.sm.update('status_text', 'obby')
            self.state = 3
            return True

        return False

    # Check for points earned text and handle state transitions
    def _check_point(self) -> bool:

        # After finishing RLGL
        if self.state == 2 and self.color.region_check(
            [self.config.TEXT_POS.x, self.config.TEXT_POS.y, 3],
            self.config.POINT_COL
        ):
            # the lazy people checks
            if self.config.STOP_RLGL:
                self.stop()
                return
            self.release_keys()
            self.sm.update('status_text', 'finished')
            self.state = 4  # Prevent immediate movement
            self.sleep(5)

            # Ensure it cannot enter "In Lobby" immediately
            self.sm.update('status_text', 'wait lob')
            previous_state = self.color.region_check(
                [self.config.LOBBY_POS.x, self.config.LOBBY_POS.y, 2],
                self.config.LOBBY_COL
            )

            # Wait until the color state changes, confirming lobby reset
            while True:
                current_state = self.color.region_check(
                    [self.config.LOBBY_POS.x, self.config.LOBBY_POS.y, 2],
                    self.config.LOBBY_COL
                )
                if current_state != previous_state:
                    break
                time.sleep(1)

            # Go idle instead of moving in the lobby
            self.sm.update('status_text', 'idle')
            self.state = 1
            return True

        # After finishing Obby
        elif self.state == 3 and self.color.region_check(
            [self.config.TEXT_POS.x, self.config.TEXT_POS.y, 3],
            self.config.POINT_COL
        ):
            self.release_keys()
            self.sm.update('status_text', 'reset')
            self.moverel(self.config.HOME_POS.x, self.config.HOME_POS.y)
            self.click()
            self.state = 0
            self.sleep(5)
            return True

        # Default check fallback
        time.sleep(0.1)
        return False

    # check for eliminiated screen
    def _check_eliminate(self) -> bool:
        if self.color.region_check([self.config.ELIM_POS.x, self.config.ELIM_POS.y, 3], self.config.ELIM_COL):
            self.release_keys()
            self.sm.update('status_text', 'reset')
            self.moverel(self.config.ELIM_POS.x-145, self.config.ELIM_POS.y-25)
            self.click()
            self.state = 0
            self.sleep(5)
            return True
        return False

    def _check_save_error(self):
        pass

    def _check_smth_error(self):
        pass

    # rlgl automation
    def rlgl(self):

        # green light
        if self.color.region_check([self.config.RLGL_POS.x, self.config.RLGL_POS.y, 3], self.config.RLGL_GREEN, tolerance=80):
            self.sm.update('status_text', 'moving')
            self.keydown(self._orientation_key())

            # move until red
            while (self.config.RUNNING and self.color.region_check([self.config.RLGL_POS.x, self.config.RLGL_POS.y, 3], self.config.RLGL_GREEN, tolerance=80)):
                self._check_point()
                time.sleep(0.1)

        # red light
        elif self.color.region_check([self.config.RLGL_POS.x, self.config.RLGL_POS.y, 3], self.config.RLGL_RED, tolerance=30):
            self.sm.update('status_text', 'waiting')
            time.sleep(0.2) # move a bit further for free
            self.keyup(self._orientation_key())

            # stop until green
            while (self.config.RUNNING and self.color.region_check([self.config.RLGL_POS.x, self.config.RLGL_POS.y, 3], self.config.RLGL_RED, tolerance=30)):
                self._check_point()
                time.sleep(0.1)

    # obby automation
    def obby(self):
        try:
            # orientation mappings
            def translate_key(key):

                # this hurt my brain
                orientation_map = {
                    0: {'w': 'w', 'a': 'a', 's': 's', 'd': 'd'}, # facing east (default)
                    1: {'w': 's', 'a': 'd', 's': 'w', 'd': 'a'}, # facing west
                    2: {'w': 'd', 'a': 'w', 's': 'a', 'd': 's'}, # facing north
                    3: {'w': 'a', 'a': 's', 's': 'd', 'd': 'w'}, # facing south
                }
                return orientation_map[self.orientation].get(key, key)

            # go into corner
            self.keydown(translate_key('w'))
            self.sleep(4)
            self.keyup(translate_key('w'))
            self.keydown(translate_key('d'))
            self.sleep(4)
            self.keyup(translate_key('d'))
            self.keydown(translate_key('w'))
            self.sleep(1)
            self.release_keys()

            # play each keystroke
            start_time = time.time()

            # just to avoid going back to world if eliminated
            completed = True
            for action in self.config.OBBY_JSON['keystrokes']:
                if not self.config.RUNNING or self._check_eliminate():
                    completed = False
                    break

                # calculate wait time
                current_time = time.time() - start_time
                target_time = action['timestamp']
                wait_time = target_time - current_time

                if wait_time > 0:
                    time.sleep(wait_time)

                # execute keystroke
                key = translate_key(action['key'])
                if action['type'] == 'keydown':
                    self.keydown(key)
                else:
                    self.keyup(key)

            if completed:
                # the lazy people check
                if self.config.STOP_OBBY:
                    self.stop()
                    return
                time.sleep(0.5)
                self.sm.update('status_text', 'reset')
                self.moverel(self.config.HOME_POS.x, self.config.HOME_POS.y)
                self.click()
                self.state = 0
                self.sleep(5)

        except Exception as e:
            print(f'error in obby: {e}')
            self.release_keys()

    # mini games loop
    def minigames(self):

        # slight delay
        for i in range(3, 0, -1):
            if self.config.RUNNING:
                self.sm.update('status_text', f'{i}...')
                time.sleep(1)
        self.wm.activate()

        try:
            while not self.tm.stop_event.is_set() and self.config.RUNNING:

                # check disconnected
                self._check_disconnected()

                # check if spawn world
                self._check_spawn_world()

                # check game first
                self._check_game()

                # check if lobby
                self._check_lobby()

                # check for eliminated screen
                self._check_eliminate()

                # RED LIGHT.... GREEEEEEEN LIIIIIIIGGHHHTTT
                if self.state == 2:
                    self.rlgl()

                # THE OBBBYYYYYYYYYYY
                elif self.state == 3:
                    self.obby()

                # nothing
                else:
                    self.sm.update('status_text', 'idle')
                    time.sleep(0.5)

        # release key if error
        except Exception as e:
            self.release_keys()
            print(e)
        finally:
            self.release_keys()

    def start(self):
        if not self.config.RUNNING:
            self.config.RUNNING = True
            if not self.wm.wait_target_win():
                self.sm.update('status_text', 'failed')
                self.sm.update('status_text_hover', 'cant find window, select again')
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
        self.state = 0
        self.tm.stop_all_threads()
        self.sm.configure('run_button', label='START')
        self.sm.update('status_text', 'inactive')
