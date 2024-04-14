from kivy.app import App

from ..save_poketset_dropdown import SavePoketsetDropdown

def confirm_save_poketset():
    savepoketsetdropdown = SavePoketsetDropdown()
    poketset_window = App.get_running_app().root.get_screen("poketset_window")
    savepoketsetdropdown.open(poketset_window.ids.save_pokeset_btn)