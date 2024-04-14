from kivy.app import App

def reset_poketset():
    
    poketset_window = App.get_running_app().root.get_screen("poketset_window")
    #poketset_window.ids.instructions.text="Select Number of Players\nor Categories to be Randomized"
    poketset_window.ids.poketset_masterminds.text=''
    poketset_window.ids.poketset_villains.text=''
    poketset_window.ids.poketset_henchmen.text=''
    poketset_window.ids.poketset_heroes.text=''    