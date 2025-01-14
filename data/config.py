import os
from collections import namedtuple

# this is so cool
point = namedtuple('point', ['x', 'y'])

class Config:
    def __init__(self, script_dir):
        self.VERSION = 0.8
        self.RUNNING = False
        self.HWND = None
        self.WINTITLE = 'Roblox'
        self.WIDTH = 800
        self.HEIGHT = 600

        # keybinds
        self.JUMP = 'space'
        self.LEFT = 'a'
        self.RIGHT = 'd'
        self.FORWARD = 'w'
        self.BACKWARD = 's'

        # point / game name text
        self.TEXT_POS = point(404, 426)
        self.POINT_COL = (255, 255, 1)
        self.GAME_COL = (255, 47, 146)

        # home icon coords
        self.HOME_POS = point(404, 516)

        # lobby indicator (menu icon)
        self.LOBBY_POS = point(410, 530)
        self.LOBBY_COL = (252, 169, 1)

        # eliminated
        self.ELIM_POS = point(550, 560)
        self.ELIM_COL = (255, 9, 74)

        # rlgl
        self.RLGL_POS = point(393, 126)
        self.RLGL_RED = (255, 24, 24)
        self.RLGL_GREEN = (83, 250, 58)

        # rlgl orientation check
        self.RLGL_ORI_POS1 = point(150, 300)
        self.RLGL_ORI_POS2 = point(650, 300)
        self.RLGL_ORI_COL = (255, 0, 0)

        # rlgl game text position (for determining obby or not without ocr)
        self.RLGL_GAME_POS = point(304, 425)

        # obby color
        self.OBBY_POS = point(790, 590)
        self.OBBY_COL = (83, 154, 195)

        # "Something went wrong. Do you want to try re-joining?" ERROR
        self.SMTH_ERR_POS = point(360, 410)
        self.SMTH_ERR_COL = (253, 158, 66)

        # "You were kicked from this experience: [SAVING] Something went wrong. Please rejoin! (Error Code: 267)" ERROR
        self.SAVE_ERR_POS = point(220, 400)
        self.SAVE_ERR_COL1 = (57, 59, 61)
        self.SAVE_ERR_COL2 = (255, 255, 255)

        # automation file location
        self.OBBY_JSON = os.path.join(script_dir, 'macro87_1736813693.json')