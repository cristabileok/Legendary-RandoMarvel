from kivy.app import App


def go_to_keywords_description():
        app = App.get_running_app()
        app.root.get_screen("main_window").manager.transition.direction = "left"
        app.root.get_screen("main_window").manager.current = "keywords_window"