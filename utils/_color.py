import time
import win32gui
import numpy as np
from PIL import ImageGrab

class ColorDetector:
    def __init__(self, wm):
        self.wm = wm

        # captures config
        self._capture_cooldown = 0.1
        self._last_capture_time = 0
        self._last_capture = None

    # the reason i used imagegrab to directly capture the screen was because
    # roblox had some safety feature that blocked indirectly capturing the window idek man
    def capture_window(self):
        """capture window content as a numpy array for processing"""
        current_time = time.time()
        if current_time - self._last_capture_time < self._capture_cooldown:
            return self._last_capture

        hwnd = self.wm.config.HWND
        if not hwnd or not win32gui.IsWindow(hwnd):
            return None

        try:
            # get window dimensions
            rect = self.wm.get_rect()
            if not rect:
                return None

            left = rect['left']
            top = rect['top']
            right = rect['left'] + rect['width']
            bottom = rect['top'] + rect['height']

            # capture the region of the screen from window coords
            img = ImageGrab.grab(bbox=(left, top, right, bottom))

            # convert image to numpy array
            img_np = np.array(img, dtype=np.int16)

            # store result
            self._last_capture = img_np
            self._last_capture_time = current_time

            return self._last_capture

        except Exception as e:
            print(f'capture error: {e}')
            return None

    def get_pixel(self, x, y):
        """get rgb color at coords"""
        capture = self.capture_window()
        if capture is None or y >= capture.shape[0] or x >= capture.shape[1]:
            return None
        color = capture[y, x]
        return color

    def check(self, x, y, target_color, tolerance=10) -> bool:
        """check if color at coords match target within tolerance"""
        color = self.get_pixel(x, y)
        if color is None:
            return False
        target = np.array(target_color, dtype=np.int16)
        return np.all(np.abs(color - target) <= tolerance)

    def region_check(self, color, region, tolerance=10):
        """find first occurrence of color in region (x1, y1, x2, y2)"""
        capture = self.capture_window()
        if capture is None:
            return None

        # set region
        x1, y1, x2, y2 = region
        search_area = capture[y1:y2, x1:x2]

        # convert to int16
        color_array = np.array(color, dtype=np.int16).reshape(1, 1, 3)

        # make mask where color matches within tolerance
        color_mask = np.all(np.abs(search_area - color_array) <= tolerance, axis=2)

        # find matching coords
        matches = np.where(color_mask)
        if len(matches[0]) > 0:

            # return first match, also adjusted for region offset
            return (matches[1][0] + x1, matches[0][0] + y1)

        return None