from collections import namedtuple

# this is so cool
point = namedtuple('point', ['x', 'y'])

class Config:
    def __init__(self):
        self.VERSION = 0.5
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

        # text coords
        self.TEXT_POS = point(404, 426)
        self.POINT_COL = (255, 255, 1)

        # game text coords
        self.RLGL_GAME_POS = point(315, 426)
        self.GAME_COL = (253, 48, 145)

        # lobby indicator (menu icon)
        self.LOBBY_POS = point(410, 530)
        self.LOBBY_COL = (252, 169, 1)

        # home icon coords
        self.HOME_POS = point(404, 516)

        # eliminated
        self.ELIM_POS = point(550, 560)
        self.ELIM_COL = (255, 9, 74)

        # rlgl colors
        self.RLGL_POS = point(396, 128)
        self.RLGL_RED = (255, 24, 24)
        self.RLGL_GREEN = (83, 255, 56)
        self.RLGL_COL = (230, 235, 157)

        # rlgl orientation check
        self.RLGL_ORI_POS1 = point(150, 300)
        self.RLGL_ORI_POS2 = point(650, 300)
        self.RLGL_ORI_COL = (255, 0, 0)

        # obby color
        self.OBBY_POS = point(790, 590)
        self.OBBY_COL = (83, 154, 195)