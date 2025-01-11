import dearpygui.dearpygui as dpg

def create_gui(automation):
    dpg.create_context()

    def aot_callback():
        dpg.set_viewport_always_top(dpg.get_value('always_on_top'))

    with dpg.window(tag='main'):
         with dpg.tab_bar():
            with dpg.tab(label='main'):
                dpg.add_spacer(height=0.5)
                with dpg.group(horizontal=True):
                    with dpg.group():
                        dpg.add_checkbox(label='anti-afk', tag='anti_afk', default_value=False, enabled=False)
                        with dpg.tooltip(dpg.last_item()):
                            dpg.add_text('disabled for this war')

                        dpg.add_checkbox(label='always on top', tag='always_on_top', 
                                       default_value=True, callback=aot_callback)
                        with dpg.tooltip(dpg.last_item()):
                            dpg.add_text('keep this window on top')

                        #dpg.add_checkbox(label='disable rmb', tag='disable_rmb', default_value=True, callback=rmb_callback)
                        #with dpg.tooltip(dpg.last_item()):
                        #    dpg.add_text('no right click to avoid accidentally moving the camera angle', wrap=240)
                        dpg.add_text('...')

                        dpg.add_spacer(height=2)
                        with dpg.group(horizontal=True):
                            dpg.add_text('status:')
                            dpg.add_text('inactive', color=(100, 149, 238), tag='status_text')
                            with dpg.tooltip(dpg.last_item()):
                                dpg.add_text('Waiting to start...', tag='status_text_hover')

                    dpg.add_spacer(width=17)
                    with dpg.group():
                        dpg.add_button(label='START', tag='run_button', width=91, height=91, callback=lambda: automation.start())

            with dpg.tab(label='instructions'):
                dpg.add_spacer(height=0.5)
                dpg.add_text('join event world', bullet=True)
                dpg.add_text('click START button', bullet=True)
                dpg.add_text('Click the target window when prompted', bullet=True)
