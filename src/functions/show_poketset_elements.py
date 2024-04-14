from kivy.app import App

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

from .randomize_list import randomize_list
from .adjust_poketset_to_input import adjust_poketset_to_mastermind, adjust_poketset_to_villain, adjust_poketset_to_henchman

    
def show_poketset_randomized_mastermind(num):
    poketset_window = App.get_running_app().root.get_screen("poketset_window")
    new_randomized_list = randomize_list(masterminds_names,num).replace("Epic ","")
    poketset_window.ids.poketset_masterminds.text = "{}".format(new_randomized_list)
    adjust_poketset_to_mastermind(new_randomized_list)
    return(new_randomized_list)
    

def show_poketset_randomized_villains(num):
    poketset_window = App.get_running_app().root.get_screen("poketset_window")
    new_randomized_list = randomize_list(villains_names,num)
    poketset_window.ids.poketset_villains.text = "{}".format(new_randomized_list)
    adjust_poketset_to_villain(new_randomized_list)
    return(new_randomized_list)


def show_poketset_randomized_henchmen(num):
    poketset_window = App.get_running_app().root.get_screen("poketset_window")
    new_randomized_list = randomize_list(henchmen_names,num)
    poketset_window.ids.poketset_henchmen.text = "{}".format(new_randomized_list)
    adjust_poketset_to_henchman(new_randomized_list)
    return(new_randomized_list)

def show_poketset_randomized_heroes(num):
    poketset_window = App.get_running_app().root.get_screen("poketset_window")
    poketset_window.ids.poketset_heroes.text = "{}".format(randomize_list(heroes_names,num))
