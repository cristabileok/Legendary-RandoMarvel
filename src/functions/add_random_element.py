import os

from kivy.app import App

from .show_elements import *

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

def add_random_element(type,*game_setup_heroes):
    main_window = App.get_running_app().root.get_screen("main_window")
    poketset_switch = main_window.ids.poketset_switch   
    
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


        if not poketset_switch.active:
            while len(old_set) == old_length and len(old_set) < len(type):
                old_set.add(str(randomize_list(type,1)))
        else:
            poketset = open(os.path.join(os.path.dirname(__file__),'../../lists/saved_poketset.txt'), 'r')
            if len(poketset.read().splitlines()) != 4:
                pass

            else:
                poketset = open(os.path.join(os.path.dirname(__file__),'../../lists/saved_poketset.txt'), 'r')
                poketset_masterminds, poketset_villains, poketset_henchmen, poketset_heroes = poketset.read().splitlines()
                poketset_masterminds = poketset_masterminds.split(" / ")
                poketset_villains = poketset_villains.split(" / ")
                poketset_henchmen = poketset_henchmen.split(" / ")
                poketset_heroes = poketset_heroes.split(" / ")

                if type == masterminds_names:
                    poketset_type = poketset_masterminds
                elif type == villains_names:
                    poketset_type = poketset_villains
                elif type == henchmen_names:
                    poketset_type = poketset_henchmen
                elif type == heroes_names:
                    poketset_type = poketset_heroes
                
                while len(old_set) == old_length and len(old_set) < len(poketset_type):
                    old_set.add(str(randomize_list(type,1)))
            
        old_set = sorted(old_set)
        new_text = " / ".join(old_set)
        
        if type == masterminds_names:
            main_window.ids.mastermind_lab.text = "{}".format(new_text)
        elif type == villains_names:
            main_window.ids.villains_lab.text = "{}".format(new_text)
        elif type == henchmen_names:
            main_window.ids.henchmen_lab.text = "{}".format(new_text)
        elif type == heroes_names:
            main_window.ids.heroes_lab.text = "{}".format(new_text)