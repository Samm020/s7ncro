import dearpygui.dearpygui as dpg
import sys
from utils._gui import create_gui
from utils._sm import StatusManager
from utils._tm import ThreadManager
from utils._wm import WindowManager
from utils._auto import Automation
from utils._update import AutoUpdate
from data.config import Config

if __name__ == '__main__':
    config = Config()
    sm = StatusManager()
    tm = ThreadManager()
    wm = WindowManager(config, sm)
    automation = Automation(config, sm, tm, wm)

    # auto update
    update = AutoUpdate(
        repo_owner=config.REPO_OWNER,
        repo_name=config.REPO_NAME,
        current_version=config.VERSION
    )

    # setup gui and start
    create_gui(automation, config, update)
    dpg.create_viewport(title=f'squid v{config.VERSION}', min_width=270, min_height=176, width=270, height=176, resizable=False)
    dpg.set_viewport_always_top(True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window('main', True)
    dpg.start_dearpygui()

    # kill all threads
    tm.stop_all_threads()
    dpg.destroy_context()
    sys.exit(0)
