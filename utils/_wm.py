import win32gui
import win32con
import time

class WindowManager:
    def __init__(self, config, sm):
        self.config = config
        self.sm = sm

    def wait_target_win(self) -> bool:
        self.sm.update('status_text', 'select')
        self.sm.update('status_text_hover', 'click the target window')

        # wait for user to select target window
        while self.config.HWND is None and self.config.RUNNING:
            time.sleep(0.1)
            active_hwnd = win32gui.GetForegroundWindow()
            if win32gui.GetWindowText(active_hwnd) == self.config.WINTITLE:
                self.config.HWND = active_hwnd
                break

        if self.config.HWND and win32gui.IsWindow(self.config.HWND):
            self.sm.update('status_text', 'selected')
            self.sm.update('status_text_hover',  f'target: {self.config.HWND}')
            rect = win32gui.GetWindowRect(self.config.HWND)
            x = rect[0]
            y = rect[1]
            win32gui.SetWindowPos(self.config.HWND, None, x, y, 
                                self.config.WIDTH, self.config.HEIGHT, 
                                win32con.SWP_SHOWWINDOW)
            return True
        return False
    
    def exist(self) -> bool:
        """check if the window exists"""
        return bool(self.config.HWND and win32gui.IsWindow(self.config.HWND))

    def activate(self):
        """activate the target window"""
        if self.exist():
            win32gui.SetForegroundWindow(self.config.HWND)

    def get_rect(self):
        """get target window dimensions"""
        if self.exist():
            rect = win32gui.GetClientRect(self.config.HWND)
            point = win32gui.ClientToScreen(self.config.HWND, (0, 0))
            return {
                'left': point[0],
                'top': point[1],
                'width': rect[2],
                'height': rect[3]
            }
