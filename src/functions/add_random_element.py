from kivy.app import App

from .show_elements import *

from ..database import (
    masterminds_names,
    schemes_names,
    villains_names,
    henchmen_names,
    heroes_names,
    keywords_dict,
    masterminds_dict,
    villains_dict,
    henchmen_dict,
    heroes_dict,
    schemes_dict_desc,
    schemes_dict_keys,
    keywords_names
)

def add_random_element(type,*game_setup_heroes):
    main_window = App.get_running_app().root.get_screen("main_window")
    if type == masterminds_names:
        old_text = main_window.ids.mastermind_lab.text
    elif type == villains_names:
        old_text = main_window.ids.villains_lab.text
    elif type == henchmen_names:
        old_text = main_window.ids.henchmen_lab.text
    elif type == heroes_names:
        old_text = main_window.ids.heroes_lab.text
        
    if old_text == "":
        if type == masterminds_names:
            show_randomized_mastermind(1)
        elif type == villains_names:
            show_randomized_villains(1)
        elif type == henchmen_names:
            show_randomized_henchmen(1,game_setup_heroes)
        elif type == heroes_names:
            show_randomized_heroes(1)
            
    else:        
        old_set = set(old_text.split(" / "))
        
        old_length = len(old_set)
        
        while len(old_set) == old_length and len(old_set) < len(type):
            old_set.add(str(randomize_list(type,1)))
            
        new_text = " / ".join(old_set)
        
        if type == masterminds_names:
            main_window.ids.mastermind_lab.text = "{}".format(new_text)
        elif type == villains_names:
            main_window.ids.villains_lab.text = "{}".format(new_text)
        elif type == henchmen_names:
            main_window.ids.henchmen_lab.text = "{}".format(new_text)
        elif type == heroes_names:
            main_window.ids.heroes_lab.text = "{}".format(new_text)