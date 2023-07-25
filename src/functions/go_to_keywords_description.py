from kivy.app import App


def go_to_keywords_description(btn):
        
        app = App.get_running_app()
        target_screen = app.root.get_screen("keywords_window")
        app.root.get_screen("main_window").manager.transition.direction = "left"
        app.onNextScreen(btn,target_screen)