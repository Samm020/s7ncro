from collections import namedtuple

# this is so cool
point = namedtuple('point', ['x', 'y'])

class Config:
    def __init__(self):
        self.VERSION = '1.3'
        self.REPO_OWNER = 'phruut'
        self.REPO_NAME = 's7ncro'

        self.RUNNING = False
        self.HWND = None
        self.WINTITLE = 'Roblox'
        self.WIDTH = 800
        self.HEIGHT = 600

        # for lazy people
        self.STOP_RLGL = False
        self.STOP_OBBY = False

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

        # orientation checks...
        self.RLGL_ORI_POS_ML = point(280, 240) # middle
        self.RLGL_ORI_POS_MR = point(520, 240) # expand 40 pixels

        self.RLGL_ORI_POS_LX = point(1, 310) # left and right sides tpo left bottom right
        self.RLGL_ORI_POS_LY = point(120, 400)
        self.RLGL_ORI_POS_RX = point(680, 310)
        self.RLGL_ORI_POS_RY = point(800, 400)

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

        # New spawn world specific detection
        self.W1_BLOCK_POS = point(389, 505)
        self.W1_BLOCK_COL = (21, 221, 206)

        # teleport button
        self.TELEPORT_POS = point(108, 190)

        # reconnect
        self.RECONNECT_POS = point(420, 380)
        self.RECONNECT_COL = (255, 255, 255)
        self.LEAVE_POS = point(360, 380)
        self.LEAVE_COL = (57, 59, 61)

        # obby automation
        self.OBBY_JSON = {
        "keystrokes": [
        {
        "timestamp": 0.813,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 4.313,
        "type": "keydown",
        "key": "w"
        },
        {
        "timestamp": 4.344,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 6.329,
        "type": "keyup",
        "key": "w"
        },
        {
        "timestamp": 6.485,
        "type": "keydown",
        "key": "d"
        },
        {
        "timestamp": 7.5,
        "type": "keyup",
        "key": "d"
        },
        {
        "timestamp": 7.75,
        "type": "keydown",
        "key": "d"
        },
        {
        "timestamp": 8.266,
        "type": "keyup",
        "key": "d"
        },
        {
        "timestamp": 8.407,
        "type": "keydown",
        "key": "d"
        },
        {
        "timestamp": 9.625,
        "type": "keyup",
        "key": "d"
        },
        {
        "timestamp": 9.985,
        "type": "keydown",
        "key": "d"
        },
        {
        "timestamp": 10.063,
        "type": "keyup",
        "key": "d"
        },
        {
        "timestamp": 10.313,
        "type": "keydown",
        "key": "d"
        },
        {
        "timestamp": 11.391,
        "type": "keyup",
        "key": "d"
        },
        {
        "timestamp": 12.61,
        "type": "keydown",
        "key": "d"
        },
        {
        "timestamp": 12.657,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 13.016,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 13.204,
        "type": "keyup",
        "key": "d"
        },
        {
        "timestamp": 13.375,
        "type": "keydown",
        "key": "d"
        },
        {
        "timestamp": 13.485,
        "type": "keydown",
        "key": "w"
        },
        {
        "timestamp": 13.938,
        "type": "keyup",
        "key": "w"
        },
        {
        "timestamp": 13.969,
        "type": "keyup",
        "key": "d"
        },
        {
        "timestamp": 14.094,
        "type": "keydown",
        "key": "d"
        },
        {
        "timestamp": 14.25,
        "type": "keyup",
        "key": "d"
        },
        {
        "timestamp": 14.547,
        "type": "keydown",
        "key": "d"
        },
        {
        "timestamp": 14.625,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 14.938,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 15.0,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 15.141,
        "type": "keyup",
        "key": "d"
        },
        {
        "timestamp": 15.282,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 15.454,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 15.579,
        "type": "keydown",
        "key": "space"
        },
        {
        "timestamp": 15.86,
        "type": "keyup",
        "key": "space"
        },
        {
        "timestamp": 18.047,
        "type": "keydown",
        "key": "d"
        },
        {
        "timestamp": 18.094,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 20.438,
        "type": "keydown",
        "key": "space"
        },
        {
        "timestamp": 20.625,
        "type": "keyup",
        "key": "space"
        },
        {
        "timestamp": 21.0,
        "type": "keydown",
        "key": "space"
        },
        {
        "timestamp": 21.219,
        "type": "keyup",
        "key": "space"
        },
        {
        "timestamp": 23.407,
        "type": "keyup",
        "key": "d"
        },
        {
        "timestamp": 23.438,
        "type": "keydown",
        "key": "w"
        },
        {
        "timestamp": 27.688,
        "type": "keyup",
        "key": "w"
        },
        {
        "timestamp": 27.922,
        "type": "keydown",
        "key": "w"
        },
        {
        "timestamp": 28.047,
        "type": "keyup",
        "key": "w"
        },
        {
        "timestamp": 28.282,
        "type": "keydown",
        "key": "w"
        },
        {
        "timestamp": 28.344,
        "type": "keyup",
        "key": "w"
        },
        {
        "timestamp": 28.579,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 29.516,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 29.594,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 29.766,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 30.016,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 30.032,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 30.172,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 30.282,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 30.454,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 30.579,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 30.844,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 30.891,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 31.0,
        "type": "keydown",
        "key": "space"
        },
        {
        "timestamp": 31.079,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 31.25,
        "type": "keyup",
        "key": "space"
        },
        {
        "timestamp": 31.297,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 32.188,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 32.204,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 32.329,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 32.594,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 32.625,
        "type": "keydown",
        "key": "space"
        },
        {
        "timestamp": 32.797,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 32.844,
        "type": "keyup",
        "key": "space"
        },
        {
        "timestamp": 33.172,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 33.282,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 33.282,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 33.454,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 33.594,
        "type": "keydown",
        "key": "space"
        },
        {
        "timestamp": 33.813,
        "type": "keyup",
        "key": "space"
        },
        {
        "timestamp": 33.891,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 33.985,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 34.172,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 34.375,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 34.532,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 34.704,
        "type": "keydown",
        "key": "w"
        },
        {
        "timestamp": 34.782,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 35.063,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 35.157,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 35.297,
        "type": "keydown",
        "key": "space"
        },
        {
        "timestamp": 35.36,
        "type": "keyup",
        "key": "w"
        },
        {
        "timestamp": 35.688,
        "type": "keyup",
        "key": "space"
        },
        {
        "timestamp": 35.782,
        "type": "keydown",
        "key": "w"
        },
        {
        "timestamp": 35.985,
        "type": "keyup",
        "key": "w"
        },
        {
        "timestamp": 36.344,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 36.532,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 36.672,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 36.86,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 36.938,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 37.032,
        "type": "keydown",
        "key": "space"
        },
        {
        "timestamp": 37.25,
        "type": "keyup",
        "key": "space"
        },
        {
        "timestamp": 37.297,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 37.469,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 37.797,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 37.797,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 37.844,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 38.11,
        "type": "keydown",
        "key": "space"
        },
        {
        "timestamp": 38.36,
        "type": "keyup",
        "key": "space"
        },
        {
        "timestamp": 38.579,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 38.782,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 39.0,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 39.235,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 39.36,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 39.75,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 40.313,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 40.547,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 40.672,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 40.797,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 40.829,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 41.032,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 41.125,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 41.391,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 41.516,
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
        "key": "space"
        },
        {
        "timestamp": 42.36,
        "type": "keyup",
        "key": "space"
        },
        {
        "timestamp": 42.719,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 42.719,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 42.891,
        "type": "keydown",
        "key": "w"
        },
        {
        "timestamp": 42.938,
        "type": "keydown",
        "key": "space"
        },
        {
        "timestamp": 43.172,
        "type": "keyup",
        "key": "w"
        },
        {
        "timestamp": 43.188,
        "type": "keyup",
        "key": "space"
        },
        {
        "timestamp": 43.469,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 43.625,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 43.797,
        "type": "keydown",
        "key": "space"
        },
        {
        "timestamp": 43.829,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 44.032,
        "type": "keyup",
        "key": "space"
        },
        {
        "timestamp": 44.5,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 44.547,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 44.672,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 44.766,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 45.0,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 45.063,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 45.36,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 45.407,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 45.797,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 45.86,
        "type": "keydown",
        "key": "space"
        },
        {
        "timestamp": 46.0,
        "type": "keydown",
        "key": "d"
        },
        {
        "timestamp": 46.11,
        "type": "keyup",
        "key": "space"
        },
        {
        "timestamp": 46.188,
        "type": "keyup",
        "key": "d"
        },
        {
        "timestamp": 46.485,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 46.579,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 46.704,
        "type": "keydown",
        "key": "space"
        },
        {
        "timestamp": 46.813,
        "type": "keydown",
        "key": "w"
        },
        {
        "timestamp": 46.922,
        "type": "keyup",
        "key": "space"
        },
        {
        "timestamp": 47.0,
        "type": "keyup",
        "key": "w"
        },
        {
        "timestamp": 47.344,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 47.5,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 47.579,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 47.688,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 47.766,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 47.938,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 48.047,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 48.657,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 48.75,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 48.829,
        "type": "keydown",
        "key": "space"
        },
        {
        "timestamp": 49.172,
        "type": "keyup",
        "key": "space"
        },
        {
        "timestamp": 49.36,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 49.469,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 49.641,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 49.735,
        "type": "keydown",
        "key": "a"
        },
        {
        "timestamp": 49.844,
        "type": "keyup",
        "key": "a"
        },
        {
        "timestamp": 49.86,
        "type": "keyup",
        "key": "s"
        },
        {
        "timestamp": 50.063,
        "type": "keydown",
        "key": "s"
        },
        {
        "timestamp": 50.25,
        "type": "keydown",
        "key": "space"
        },
        {
        "timestamp": 50.547,
        "type": "keyup",
        "key": "space"
        },
        {
        "timestamp": 51.094,
        "type": "keydown",
        "key": "space"
        },
        {
        "timestamp": 51.329,
        "type": "keyup",
        "key": "space"
        },
        {
        "timestamp": 51.86,
        "type": "keyup",
        "key": "s"
        }
    ]
    }