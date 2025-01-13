import time
import win32gui
import numpy as np
import mss
from ._dpi import DPIScale
from PIL import Image

class ColorDetector:
    def __init__(self, wm):
        self.wm = wm

        # captures config
        self._capture_cooldown = 0.1
        self._last_capture_time = 0
        self._last_capture = None

    # roblox had some safety feature that blocked indirectly capturing the window idek man
    def capture_window(self):
        """capture window content as a numpy array for processing."""
        current_time = time.time()
        if current_time - self._last_capture_time < self._capture_cooldown:
            return self._last_capture

        hwnd = self.wm.config.HWND
        if not hwnd or not win32gui.IsWindow(hwnd):
            return None

        try:
            # get window dims
            rect = self.wm.get_rect()
            if not rect:
                return None

            left = rect['left']
            top = rect['top']
            right = left + rect['width']
            bottom = top + rect['height']

            # addjust for dpi scaling
            scaling_factor = DPIScale.get_scaling_factor()
            left, top, right, bottom = DPIScale.adjust_for_scaling([left, top, right, bottom], scaling_factor)

            # use new mss instance for each capture because it caused threading issues
            with mss.mss() as cpt:
                monitor = {'top': top, 'left': left, 'width': right - left, 'height': bottom - top}
                capture = cpt.grab(monitor)

            # convert the image to a numpy array, reorder BGRA to RGB
            img_np = np.array(capture, dtype=np.uint8)[:, :, :3]
            img_np = img_np[:, :, ::-1]

            # store result
            self._last_capture = img_np
            self._last_capture_time = current_time
            
            img = Image.fromarray(img_np)
            img.save('screenshot.png')

            return self._last_capture

        except Exception as e:
            print(f'capture error: {e}')
            return None

    def get_pixel(self, x, y):
        """get rgb color at coords"""
        capture = self.capture_window()
        if capture is None or y >= capture.shape[0] or x >= capture.shape[1]:
            return None
        return capture[y, x]

    def check(self, x, y, target_color, tolerance=10) -> bool:
        """check if color at coords match target within tolerance"""
        color = self.get_pixel(x, y)
        if color is None:
            return False
        target = np.array(target_color, dtype=np.uint8)
        return np.all(np.abs(color - target) <= tolerance)

    def region_check(self, region, color, tolerance=10) -> bool:
        """find first occurrence of color in region (x, y, expand) or (x1, y1, x2, y2)"""
        capture = self.capture_window()
        if capture is None:
            return False

        # coord with expand value
        if len(region) == 3:
            x, y, e = region
            x1 = x - e
            y1 = y - e
            x2 = x + e
            y2 = y + e

        # specified region
        elif len(region) == 4:
            x1, y1, x2, y2 = region
        else:
            raise ValueError('bad region format, must be (x1, y1, x2, y2) or (x, y, expand)')
        search_area = capture[y1:y2, x1:x2]

        # convert to uint8
        color_array = np.array(color, dtype=np.uint8).reshape(1, 1, 3)

        # make mask where color matches within tolerance
        color_mask = np.all(np.abs(search_area - color_array) <= tolerance, axis=2)

        # find matching coords
        matches = np.where(color_mask)
        if len(matches[0]) > 0:

            # return first match, also adjusted for region offset
            return (matches[1][0] + x1, matches[0][0] + y1)

        return False
