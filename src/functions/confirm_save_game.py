from kivy.app import App

from ..save_game_dropdown import SaveGameDropdown

def confirm_save_game(number_of_villains,number_of_henchmen,number_of_heroes):
    savegamedropdown = SaveGameDropdown(number_of_villains,number_of_henchmen,number_of_heroes)
    main_window = App.get_running_app().root.get_screen("main_window")
    savegamedropdown.open(main_window.ids.save_game_btn)


