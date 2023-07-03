from kivy.app import App

from .create_this_scheme_description import create_this_scheme_description


def go_to_scheme_description():
    main_window = App.get_running_app().root.get_screen("main_window")
    scheme = main_window.ids.scheme_lab.text
    create_this_scheme_description(scheme)