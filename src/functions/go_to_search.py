from kivy.app import App

def go_to_search():
    app = App.get_running_app()
    app.root.get_screen("main_window").manager.transition.direction = "left"
    app.root.get_screen("main_window").manager.current = "search_window"
    app.root.get_screen("search_window").ids.textinput.focus=True