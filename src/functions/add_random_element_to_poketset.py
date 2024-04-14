import os

from kivy.app import App

from .randomize_list import randomize_list
from .show_poketset_elements import show_poketset_randomized_henchmen, show_poketset_randomized_heroes, show_poketset_randomized_mastermind, show_poketset_randomized_villains
from .adjust_poketset_to_input import adjust_poketset_to_mastermind, adjust_poketset_to_villain, adjust_poketset_to_henchman


from ..database import (
    masterminds_names,
    schemes_names,
    villains_names,
    henchmen_names,
    heroes_names,
    keywords_dict,
    masterminds_to_keywords,
    villains_dict,
    henchmen_dict,
    heroes_dict,
    schemes_dict_desc,
    schemes_dict_keys,
    keywords_names
)

def add_random_element_to_poketset(type,*game_setup_heroes):
    poketset_window = App.get_running_app().root.get_screen("poketset_window")
    
    
    if type == masterminds_names:
        old_text = poketset_window.ids.poketset_masterminds.text
    elif type == villains_names:
        old_text = poketset_window.ids.poketset_villains.text
    elif type == henchmen_names:
        old_text = poketset_window.ids.poketset_henchmen.text
    elif type == heroes_names:
        old_text = poketset_window.ids.poketset_heroes.text
        
    if old_text == "":
        if type == masterminds_names:
            show_poketset_randomized_mastermind(1)     
        elif type == villains_names:
            show_poketset_randomized_villains(1)
        elif type == henchmen_names:
            show_poketset_randomized_henchmen(1)
        elif type == heroes_names:
            show_poketset_randomized_heroes(1)

            
    if old_text != "":        
        old_set = set(old_text.split(" / "))
        old_length = len(old_set)
        elements_added = set()

        while len(old_set) == old_length and len(old_set) < len(type):
            new_element = str(randomize_list(type,1))
            old_set.add(new_element)
            elements_added.add(new_element)
                    
        old_set = sorted(old_set)
        new_text = " / ".join(old_set)
        
        if type == masterminds_names:
            new_text = new_text.replace("Epic ","")
            poketset_window.ids.poketset_masterminds.text = "{}".format(new_text)
            adjust_poketset_to_mastermind(" / ".join(elements_added))
        elif type == villains_names:
            poketset_window.ids.poketset_villains.text = "{}".format(new_text)
            adjust_poketset_to_villain(" / ".join(elements_added))
        elif type == henchmen_names:
            poketset_window.ids.poketset_henchmen.text = "{}".format(new_text)
            adjust_poketset_to_henchman(" / ".join(elements_added))
        elif type == heroes_names:
            poketset_window.ids.poketset_heroes.text = "{}".format(new_text)

        
        
        

        