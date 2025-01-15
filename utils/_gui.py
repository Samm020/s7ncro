import dearpygui.dearpygui as dpg

def create_gui(automation, config, update):
    dpg.create_context()
    
    def stop_rlgl_callback():
        config.STOP_RLGL = dpg.get_value('stop_rlgl')
    
    def stop_obby_callback():
        config.STOP_OBBY = dpg.get_value('stop_obby')

    def aot_callback():
        dpg.set_viewport_always_top(dpg.get_value('always_on_top'))

    with dpg.window(tag='main'):
         with dpg.tab_bar():
            with dpg.tab(label='main'):
                dpg.add_spacer(height=0.5)
                with dpg.group(horizontal=True):
                    with dpg.group():
                        dpg.add_checkbox(label='always on top', tag='always_on_top', 
                                       default_value=True, callback=aot_callback)
                        with dpg.tooltip(dpg.last_item()):
                            dpg.add_text('keep this window on top')

                        # the lazy people checkboxes
                        dpg.add_checkbox(label='stop on rlgl', tag='stop_rlgl', callback=stop_rlgl_callback)
                        with dpg.tooltip(dpg.last_item()):
                            dpg.add_text('automates up to rlgl, click start when new game to use again', wrap=200)
                        dpg.add_checkbox(label='stop on obby', tag='stop_obby', callback=stop_obby_callback)
                        with dpg.tooltip(dpg.last_item()):
                            dpg.add_text('automates up to obby, click start when new game to use again', wrap=200)

                        dpg.add_spacer(height=2)
                        with dpg.group(horizontal=True):
                            dpg.add_text('status:')
                            dpg.add_text('inactive', color=(100, 149, 238), tag='status_text')
                            with dpg.tooltip(dpg.last_item()):
                                dpg.add_text('waiting for start...', tag='status_text_hover')

                    dpg.add_spacer(width=17)
                    with dpg.group():
                        dpg.add_button(label='START', tag='run_button', width=91, height=91, callback=lambda: automation.start())

            with dpg.tab(label='setup'):
                dpg.add_spacer(height=0.5)
                dpg.add_text('enter event world', bullet=True)
                dpg.add_text('enter Pet Games lobby', bullet=True)
                with dpg.group(horizontal=True):
                    dpg.add_text('press', bullet=True)
                    dpg.add_text('START')
                    with dpg.tooltip(dpg.last_item()):
                        dpg.add_text("on 'main' tab")
                    dpg.add_text('button')
                dpg.add_text('click roblox window and wait', bullet=True)

            with dpg.tab(label='update'):
                dpg.add_spacer(height=0.5)
                dpg.add_text(f'your version: {config.VERSION}')
                dpg.add_spacer(height=0.5)

                def check_update_callback():
                    result = update.check_update()
                    if 'error' in result:
                        dpg.configure_item('update_status', default_value=f'error: {result["error"]}', color=(187, 98, 110))
                    elif result['update_available']:
                        dpg.configure_item('update_status', default_value=f'v{result["version"]} update available', color=(100, 149, 238))
                        dpg.configure_item('download_update_button', show=True)
                        dpg.set_item_user_data('download_update_button', result['download_url'])
                    else:
                        dpg.configure_item('update_status', default_value='you are running the latest version.', color=(100, 149, 238))

                def download_update_callback():
                    dpg.configure_item('update_status', default_value='downloading update...', color=(100, 149, 238))
                    update_info = update.check_update()
                    result = update.run_update(update_info['download_url'], update_info['file_name'])
                    if result['success']:
                        dpg.configure_item('update_status', default_value='downloaded, restarting...', color=(100, 149, 238))
                    else:
                        dpg.configure_item('update_status', default_value=result['error'], color=(187, 98, 110))

                dpg.add_button(label='check for update', callback=check_update_callback)
                dpg.add_text('', tag='update_status')
                dpg.add_button(label='install', tag='download_update_button', show=False, callback=download_update_callback)
                