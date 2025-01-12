# ill set up a proper one later

class Config:
    def __init__(self):
        self.VERSION = 0.4
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
        self.TEXT_X = 404
        self.TEXT_Y = 426
        self.POINT_COL = (255, 255, 1)

        # game text coords
        self.RLGL_GAME_X = 315
        self.RLGL_GAME_Y = 426
        self.GAME_COL = (253, 48, 145)

        # lobby indicator (menu icon)
        self.LOBBY_X = 420
        self.LOBBY_Y = 535
        self.LOBBY_COL = (210, 235, 35)

        # home icon coords
        self.HOME_X = 404
        self.HOME_Y = 516

        # eliminated
        self.ELIM_X = 550
        self.ELIM_Y = 560
        self.ELIM_COL = (255, 9, 74)

        # rlgl colors
        self.RLGL_X = 396
        self.RLGL_Y = 128
        self.RLGL_RED = (255, 24, 24)
        self.RLGL_GREEN = (83, 255, 56)
        self.RLGL_COL = (230, 235, 157)

        # obby color
        self.OBBY_X = 790
        self.OBBY_Y = 590
        self.OBBY_COL = (83, 154, 195)