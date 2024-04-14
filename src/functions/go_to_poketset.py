from kivy.app import App

from .poketset_load_and_save import load_poketset


def go_to_poketset(btn):
        
    app = App.get_running_app()
    target_screen = app.root.get_screen("poketset_window")
    poketset_switch = app.root.get_screen("main_window").ids.poketset_switch
    poketset_switch.active = False
    app.root.get_screen("main_window").manager.transition.direction = "left"
    app.onNextScreen(btn,target_screen)

    load_poketset()

