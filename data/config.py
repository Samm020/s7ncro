from collections import namedtuple

# this is so cool
point = namedtuple('point', ['x', 'y'])

class Config:
    def __init__(self):
        self.VERSION = 0.6
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
        self.RLGL_GREEN = (83, 255, 56)

        # rlgl orientation check
        self.RLGL_ORI_POS1 = point(150, 300)
        self.RLGL_ORI_POS2 = point(650, 300)
        self.RLGL_ORI_COL = (255, 0, 0)

        # rlgl game text position (for determining obby or not without ocr)
        self.RLGL_GAME_POS = point(304, 425)

        # obby color
        self.OBBY_POS = point(790, 590)
        self.OBBY_COL = (83, 154, 195)