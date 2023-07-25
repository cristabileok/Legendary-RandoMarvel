from kivy.app import App

def go_to_search(btn):
    app = App.get_running_app()
    target_screen = app.root.get_screen("search_window")
    app.root.get_screen("main_window").manager.transition.direction = "left"
    app.onNextScreen(btn,target_screen)
    #app.root.get_screen("main_window").manager.current = "search_window"

    app.root.get_screen("search_window").ids.textinput.focus=True