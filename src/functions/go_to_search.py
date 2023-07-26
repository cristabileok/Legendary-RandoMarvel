from kivy.app import App
from kivy.uix.label import Label

def go_to_search(btn):
    app = App.get_running_app()
    target_screen = app.root.get_screen("search_window")
    app.root.get_screen("main_window").manager.transition.direction = "left"
    app.onNextScreen(btn,target_screen)
    #app.root.get_screen("main_window").manager.current = "search_window"

    if not app.root.get_screen("search_window").ids.search_container.children:
        app.root.get_screen("search_window").ids.textinput.focus=True
    elif isinstance(app.root.get_screen("search_window").ids.search_container.children[0] , Label):
        app.root.get_screen("search_window").ids.textinput.focus=True

    #else:
    #    print(app.root.get_screen("search_window").ids.search_container.children[0].__class__)
    #    if app.root.get_screen("search_window").ids.search_container.children[0].__class__ == "class 'kivy.uix.label.Label'":
    #        app.root.get_screen("search_window").ids.textinput.focus=True