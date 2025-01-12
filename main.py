import dearpygui.dearpygui as dpg
import sys
from utils._gui import create_gui
from utils._sm import StatusManager
from utils._tm import ThreadManager
from utils._wm import WindowManager
from utils._auto import Automation
from data.config import Config

if __name__ == '__main__':
    config = Config()
    sm = StatusManager()
    tm = ThreadManager()
    wm = WindowManager(config, sm)
    automation = Automation(config, sm, tm, wm)

    # setup gui and start
    create_gui(automation)
    dpg.create_viewport(title=f'squid-{config.VERSION}', min_width=270, min_height=176, width=270, height=176, resizable=False)
    dpg.set_viewport_always_top(True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window('main', True)
    dpg.start_dearpygui()
    dpg.destroy_context()

    # kill all threads
    tm.stop_all_threads()
    sys.exit(0)
