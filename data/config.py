from collections import namedtuple

# this is so cool
point = namedtuple('point', ['x', 'y'])

class Config:
    def __init__(self):
        self.VERSION = '0.9.6'
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

        # obby automation
        self.OBBY_JSON = {
            "keystrokes": [
                {
                "timestamp": 0.891,
                "type": "keydown",
                "key": "a"
                },
                {
                "timestamp": 4.36,
                "type": "keydown",
                "key": "w"
                },
                {
                "timestamp": 4.407,
                "type": "keyup",
                "key": "a"
                },
                {
                "timestamp": 6.172,
                "type": "keydown",
                "key": "d"
                },
                {
                "timestamp": 6.188,
                "type": "keyup",
                "key": "w"
                },
                {
                "timestamp": 6.407,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 6.625,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 6.828,
                "type": "keyup",
                "key": "d"
                },
                {
                "timestamp": 7.125,
                "type": "keydown",
                "key": "d"
                },
                {
                "timestamp": 7.297,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 7.313,
                "type": "keydown",
                "key": "w"
                },
                {
                "timestamp": 7.641,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 7.735,
                "type": "keyup",
                "key": "w"
                },
                {
                "timestamp": 7.828,
                "type": "keyup",
                "key": "d"
                },
                {
                "timestamp": 8.422,
                "type": "keydown",
                "key": "d"
                },
                {
                "timestamp": 8.578,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 8.578,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 8.891,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 9.063,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 9.063,
                "type": "keyup",
                "key": "d"
                },
                {
                "timestamp": 9.86,
                "type": "keydown",
                "key": "d"
                },
                {
                "timestamp": 10.125,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 10.25,
                "type": "keydown",
                "key": "w"
                },
                {
                "timestamp": 10.407,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 10.578,
                "type": "keyup",
                "key": "w"
                },
                {
                "timestamp": 10.625,
                "type": "keyup",
                "key": "d"
                },
                {
                "timestamp": 11.297,
                "type": "keydown",
                "key": "d"
                },
                {
                "timestamp": 11.453,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 11.453,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 11.797,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 11.953,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 11.969,
                "type": "keyup",
                "key": "d"
                },
                {
                "timestamp": 12.641,
                "type": "keydown",
                "key": "d"
                },
                {
                "timestamp": 12.875,
                "type": "keydown",
                "key": "w"
                },
                {
                "timestamp": 12.891,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 13.172,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 13.5,
                "type": "keyup",
                "key": "d"
                },
                {
                "timestamp": 13.516,
                "type": "keyup",
                "key": "w"
                },
                {
                "timestamp": 14.063,
                "type": "keydown",
                "key": "d"
                },
                {
                "timestamp": 14.157,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 14.328,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 14.594,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 14.828,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 14.875,
                "type": "keyup",
                "key": "d"
                },
                {
                "timestamp": 15.344,
                "type": "keydown",
                "key": "d"
                },
                {
                "timestamp": 15.391,
                "type": "keydown",
                "key": "w"
                },
                {
                "timestamp": 15.516,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 15.75,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 16.0,
                "type": "keyup",
                "key": "d"
                },
                {
                "timestamp": 16.032,
                "type": "keyup",
                "key": "w"
                },
                {
                "timestamp": 16.5,
                "type": "keydown",
                "key": "d"
                },
                {
                "timestamp": 16.594,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 16.735,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 17.047,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 17.078,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 17.188,
                "type": "keyup",
                "key": "d"
                },
                {
                "timestamp": 17.922,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 18.157,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 18.391,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 20.594,
                "type": "keydown",
                "key": "d"
                },
                {
                "timestamp": 20.657,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 23.0,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 23.25,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 23.282,
                "type": "keyup",
                "key": "d"
                },
                {
                "timestamp": 23.813,
                "type": "keydown",
                "key": "d"
                },
                {
                "timestamp": 23.953,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 24.188,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 24.375,
                "type": "keyup",
                "key": "d"
                },
                {
                "timestamp": 24.532,
                "type": "keydown",
                "key": "d"
                },
                {
                "timestamp": 26.5,
                "type": "keydown",
                "key": "w"
                },
                {
                "timestamp": 26.547,
                "type": "keyup",
                "key": "d"
                },
                {
                "timestamp": 30.578,
                "type": "keydown",
                "key": "a"
                },
                {
                "timestamp": 30.703,
                "type": "keyup",
                "key": "w"
                },
                {
                "timestamp": 31.86,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 32.328,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 32.532,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 33.172,
                "type": "keyup",
                "key": "a"
                },
                {
                "timestamp": 33.203,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 33.532,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 33.813,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 34.016,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 34.266,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 34.516,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 34.594,
                "type": "keydown",
                "key": "a"
                },
                {
                "timestamp": 34.625,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 34.735,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 34.844,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 34.953,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 35.375,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 35.422,
                "type": "keyup",
                "key": "a"
                },
                {
                "timestamp": 35.594,
                "type": "keydown",
                "key": "a"
                },
                {
                "timestamp": 35.766,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 35.985,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 36.0,
                "type": "keydown",
                "key": "w"
                },
                {
                "timestamp": 36.219,
                "type": "keyup",
                "key": "w"
                },
                {
                "timestamp": 36.422,
                "type": "keyup",
                "key": "a"
                },
                {
                "timestamp": 36.469,
                "type": "keydown",
                "key": "w"
                },
                {
                "timestamp": 36.641,
                "type": "keydown",
                "key": "a"
                },
                {
                "timestamp": 37.063,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 37.125,
                "type": "keyup",
                "key": "w"
                },
                {
                "timestamp": 37.485,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 38.157,
                "type": "keyup",
                "key": "a"
                },
                {
                "timestamp": 38.297,
                "type": "keydown",
                "key": "a"
                },
                {
                "timestamp": 38.485,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 38.578,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 38.703,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 39.282,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 39.563,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 39.782,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 39.875,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 40.11,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 40.391,
                "type": "keyup",
                "key": "a"
                },
                {
                "timestamp": 40.672,
                "type": "keydown",
                "key": "a"
                },
                {
                "timestamp": 40.688,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 40.782,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 40.922,
                "type": "keyup",
                "key": "a"
                },
                {
                "timestamp": 41.016,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 41.078,
                "type": "keydown",
                "key": "a"
                },
                {
                "timestamp": 41.203,
                "type": "keyup",
                "key": "a"
                },
                {
                "timestamp": 41.719,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 41.938,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 42.016,
                "type": "keydown",
                "key": "a"
                },
                {
                "timestamp": 42.078,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 42.141,
                "type": "keyup",
                "key": "a"
                },
                {
                "timestamp": 42.625,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 42.719,
                "type": "keydown",
                "key": "a"
                },
                {
                "timestamp": 42.75,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 42.875,
                "type": "keyup",
                "key": "a"
                },
                {
                "timestamp": 43.0,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 43.344,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 43.453,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 43.516,
                "type": "keydown",
                "key": "a"
                },
                {
                "timestamp": 43.657,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 43.672,
                "type": "keyup",
                "key": "a"
                },
                {
                "timestamp": 43.797,
                "type": "keydown",
                "key": "a"
                },
                {
                "timestamp": 43.922,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 44.032,
                "type": "keydown",
                "key": "w"
                },
                {
                "timestamp": 44.172,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 44.375,
                "type": "keyup",
                "key": "w"
                },
                {
                "timestamp": 44.594,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 44.782,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 44.813,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 44.813,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 44.875,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 45.141,
                "type": "keyup",
                "key": "a"
                },
                {
                "timestamp": 45.36,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 45.453,
                "type": "keydown",
                "key": "a"
                },
                {
                "timestamp": 45.563,
                "type": "keyup",
                "key": "a"
                },
                {
                "timestamp": 45.672,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 45.797,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 46.094,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 46.172,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 46.282,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 46.344,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 46.578,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 46.61,
                "type": "keydown",
                "key": "d"
                },
                {
                "timestamp": 46.735,
                "type": "keyup",
                "key": "d"
                },
                {
                "timestamp": 46.86,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 46.985,
                "type": "keydown",
                "key": "a"
                },
                {
                "timestamp": 47.11,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 47.344,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 47.891,
                "type": "keyup",
                "key": "a"
                },
                {
                "timestamp": 47.907,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 48.063,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 48.219,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 48.297,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 49.078,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 49.141,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 49.578,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 49.594,
                "type": "keydown",
                "key": "a"
                },
                {
                "timestamp": 49.657,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 49.938,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 50.078,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 50.328,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 50.485,
                "type": "keyup",
                "key": "a"
                },
                {
                "timestamp": 50.5,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 50.657,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 50.782,
                "type": "keyup",
                "key": "s"
                },
                {
                "timestamp": 51.188,
                "type": "keydown",
                "key": "s"
                },
                {
                "timestamp": 51.344,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 51.61,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 52.157,
                "type": "keydown",
                "key": "space"
                },
                {
                "timestamp": 52.407,
                "type": "keyup",
                "key": "space"
                },
                {
                "timestamp": 52.86,
                "type": "keyup",
                "key": "s"
                }
            ]
            }