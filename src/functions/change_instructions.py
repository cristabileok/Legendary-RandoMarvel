from kivy.app import App

def change_instructions():
    main_window = App.get_running_app().root.get_screen("main_window")
    main_window.ids.instructions.text="Press on the Results\nto see Descriptions or Keywords"