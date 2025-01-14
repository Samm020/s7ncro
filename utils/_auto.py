import time
from ._mk import Mouse, Keyboard
from ._color import Color
import json
import os
import dearpygui.dearpygui as dpg

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

    # new lobby workaround, just moves in zig zags across the queue zone
    def _zigzag(self, direction):
        self.keyboard.press(direction)
        for _ in range(3):
            if self.config.RUNNING:
                self.keyboard.press(self.config.LEFT)
                time.sleep(0.4)
                self.keyboard.release(self.config.LEFT)
                self.keyboard.press(self.config.RIGHT)
                time.sleep(0.8)
                self.keyboard.release(self.config.RIGHT)
        self.keyboard.release(direction)

    # check if in lobby
    def _in_lobby(self):
        if self.state == 0 and self.color.region_check([self.config.LOBBY_POS.x, self.config.LOBBY_POS.y, 2], self.config.LOBBY_COL):
            self.sm.update('status_text', 'in lobby')
            self.release_keys()
            self.keyboard.press(self.config.RIGHT)
            self.sleep(9)
            self.keyboard.release(self.config.RIGHT)

            # new lobby workaround
            self._zigzag(self.config.FORWARD)
            self._zigzag(self.config.BACKWARD)

            # stop moving when done
            self.keyboard.release(self.config.RIGHT)

            # set state to prevent further action
            self.state = 1

    # check the pink game name text
    def _check_game(self):

        # if rlgl
        if self.color.region_check([self.config.RLGL_GAME_POS.x, self.config.RLGL_GAME_POS.y, 3], self.config.GAME_COL):

            # fix orientation for all directions (scans for the position of red start line)
            self.keyboard.keypress('tab')
            pos1 = [self.config.RLGL_ORI_POS1.x, self.config.RLGL_ORI_POS1.y, 150]
            pos2 = [self.config.RLGL_ORI_POS2.x, self.config.RLGL_ORI_POS2.y, 150]
            color = self.config.RLGL_ORI_COL
            time.sleep(1)

            # normal left orientation
            if self.color.region_check(pos1, color) and not self.color.region_check(pos2, color):
                self.orientation = 0

            # right orientation
            elif not self.color.region_check(pos1, color) and self.color.region_check(pos2, color):
                self.orientation = 1

            # forward orientation
            elif self.color.region_check(pos1, color) and self.color.region_check(pos2, color):
                self.orientation = 2

            # backwards orientation
            elif not self.color.region_check(pos1, color) and not self.color.region_check(pos2, color):
                self.orientation = 3

            self.sm.update('status_text', 'rlgl')
            self.keyboard.press(self._orientation_key())
            self.state = 2
            self.sleep(8)

        # if obby
        elif self.color.region_check([self.config.TEXT_POS.x, self.config.TEXT_POS.y, 3], self.config.GAME_COL):
            self.sm.update('status_text', 'obby')
            self.keyboard.press(self.config.RIGHT)
            self.keyboard.press(self.config.FORWARD)
            self.state = 3
            self.sleep(9)

    # check for points earned text
    def _check_point(self):
        if self.state == 2 and self.color.region_check([self.config.TEXT_POS.x, self.config.TEXT_POS.y, 3], self.config.POINT_COL):
            # Make sure to release ALL keys from RLGL first
            self.release_keys()
            self.sm.update('status_text', 'transitioning to obby')
            time.sleep(0.5)  # Small pause to ensure all keys are released
            
            # Set state before pressing new keys
            self.state = 3  # Set state to obby directly
            self.sleep(0.1)  # Small pause to ensure state is set

    # check for eliminiated screen
    def _check_eliminate(self):
        if self.color.region_check([self.config.ELIM_POS.x, self.config.ELIM_POS.y, 3], self.config.ELIM_COL):
            self.release_keys()
            self.sm.update('status_text', 'reset')
            self.moverel(self.config.ELIM_POS.x-150, self.config.ELIM_POS.y-25)
            self.mouse.click()
            self.state = 0
            self.sleep(9)
    
    def _check_save_error(self):
        pass
    
    def _check_smth_error(self):
        pass

    # rlgl automation
    def rlgl(self):
        # green light
        if self.color.region_check([self.config.RLGL_POS.x, self.config.RLGL_POS.y, 3], self.config.RLGL_GREEN, tolerance=80):
            self.sm.update('status_text', 'moving')
            self.keyboard.press(self._orientation_key())

            # move until red or points earned
            while (self.config.RUNNING and 
                   self.color.region_check([self.config.RLGL_POS.x, self.config.RLGL_POS.y, 3], self.config.RLGL_GREEN, tolerance=80)):
                # If we earned points, break out immediately
                if self.color.region_check([self.config.TEXT_POS.x, self.config.TEXT_POS.y, 3], self.config.POINT_COL):
                    self._check_point()
                    return  # Exit RLGL immediately
                time.sleep(0.1)

        # red light
        elif self.color.region_check([self.config.RLGL_POS.x, self.config.RLGL_POS.y, 3], self.config.RLGL_RED, tolerance=30):
            self.sm.update('status_text', 'waiting')
            time.sleep(0.2) # move a bit further for free
            self.keyboard.release(self._orientation_key())

            # stop until green or points earned
            while (self.config.RUNNING and 
                   self.color.region_check([self.config.RLGL_POS.x, self.config.RLGL_POS.y, 3], self.config.RLGL_RED, tolerance=30)):
                # If we earned points, break out immediately
                if self.color.region_check([self.config.TEXT_POS.x, self.config.TEXT_POS.y, 3], self.config.POINT_COL):
                    self._check_point()
                    return  # Exit RLGL immediately
                time.sleep(0.1)
        
        # No color detected - stop moving and check if we're still in RLGL
        else:
            self.sm.update('status_text', 'no color detected')
            self.keyboard.release(self._orientation_key())
            
            # If we can't see red or green, we might be transitioning - wait a bit
            time.sleep(0.5)
            
            # If we still can't see any color and we're in RLGL state, check for points
            if (self.state == 2 and not 
                (self.color.region_check([self.config.RLGL_POS.x, self.config.RLGL_POS.y, 3], self.config.RLGL_GREEN, tolerance=80) or 
                 self.color.region_check([self.config.RLGL_POS.x, self.config.RLGL_POS.y, 3], self.config.RLGL_RED, tolerance=30))):
                self._check_point()

    # obby automation
    def obby(self):
        """Execute the obby sequence"""
        try:
            # Do the initial sequence if we just entered obby state
            if self.state == 3:
                self.sm.update('status_text', 'moving to obby position')
                self.keyboard.press(self.config.RIGHT)  # 'd'
                self.keyboard.press(self.config.FORWARD)  # 'w'
                time.sleep(9.0)  # Same wait time as automation
                self.keyboard.release(self.config.RIGHT)  # Release 'd' first
                time.sleep(0.2)  # Small pause to straighten out
                self.keyboard.release(self.config.FORWARD)  # Then release 'w'
                time.sleep(0.5)  # Small pause before starting sequence

            # Get path to recordings directory
            recordings_dir = os.path.join(os.path.dirname(__file__), 'recordings')
            macro_path = os.path.join(recordings_dir, 'macro87_1736813693.json')
            
            # Load and play the recording
            try:
                with open(macro_path, 'r') as f:
                    recording = json.load(f)
            except FileNotFoundError:
                print(f"Error: Macro file not found at {macro_path}")
                return
            except json.JSONDecodeError:
                print(f"Error: Invalid JSON in macro file {macro_path}")
                return
            
            # Play each keystroke with exact timing
            start_time = time.time()
            last_time = start_time
            
            for action in recording['keystrokes']:
                if not self.config.RUNNING:  # Stop if automation is stopped
                    break
                    
                # Calculate precise wait time
                current_time = time.time() - start_time
                target_time = action['timestamp']
                wait_time = target_time - current_time
                
                if wait_time > 0:
                    time.sleep(wait_time)
                
                # Execute the keystroke
                if action['type'] == 'keydown':
                    self.keyboard.press(action['key'])
                else:
                    self.keyboard.release(action['key'])
                
                last_time = time.time()
            
            # After keystrokes finish, go home like in eliminate
            self.release_keys()
            self.sm.update('status_text', 'going home')
            self.moverel(self.config.HOME_POS.x, self.config.HOME_POS.y)
            self.mouse.click()
            self.state = 0  # Back to lobby
            time.sleep(9)
                
        except Exception as e:
            print(f"Error in obby: {e}")
            self.release_keys()

    # mini games loop
    def minigames(self):

        # slight delay
        for i in range(3, 0, -1):
            self.sm.update('status_text', f'{i}...')
            self.sleep(1)
        self.wm.activate()

        try:
            while not self.tm.stop_event.is_set() and self.config.RUNNING:

                self._in_lobby()
                self._check_eliminate()
                self._check_game()

                # RED LIGHT.... GREEEEEEEN LIIIIIIIGGHHHTTT
                if self.state == 2:
                    self.rlgl()
                    time.sleep(0.1)

                # THE OBBBYYYYYYYYYYY
                elif self.state == 3:
                    self.sm.update('status_text', 'in obby')
                    self.obby()

                else:
                    self.sm.update('status_text', 'idle')
                    time.sleep(1)

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
                self.sm.update('status_text_hover', 'cant find window, select again')
                self.config.HWND = None
                self.config.RUNNING = False
                return
            self.sm.configure('run_button', label='STOP')
            self.tm.add_thread('minigames', self.minigames)
        else:
            self.stop()

    def stop(self):
        """Stop the automation"""
        self.release_keys()  # Release all keys first
        self.config.RUNNING = False
        
        try:
            # Try to update GUI elements, but don't crash if they don't exist
            if dpg.does_item_exist('run_button'):
                dpg.configure_item('run_button', label='START')
            if dpg.does_item_exist('status_text'):
                dpg.set_value('status_text', 'stopped')
        except:
            pass  # Ignore any DPG errors

        self.tm.stop_all_threads()
        self.state = 0
