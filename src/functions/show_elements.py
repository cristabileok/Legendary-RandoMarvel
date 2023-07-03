from kivy.app import App

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

from .randomize_list import randomize_list

def show_randomized_schemes(num):
    main_window = App.get_running_app().root.get_screen("main_window")
    main_window.ids.scheme_lab.text = "{}".format(randomize_list(schemes_names,num))
    while "|" in main_window.ids.scheme_lab.text:
        main_window.ids.scheme_lab.text = "{}".format(randomize_list(schemes_names,num))
    
def show_randomized_mastermind(num):
    main_window = App.get_running_app().root.get_screen("main_window")
    main_window.ids.mastermind_lab.text = "{}".format(randomize_list(masterminds_names,num))

def show_randomized_villains(num):
    main_window = App.get_running_app().root.get_screen("main_window")
    main_window.ids.villains_lab.text = "{}".format(randomize_list(villains_names,num))

def show_randomized_henchmen(num,game_setup_heroes):
    main_window = App.get_running_app().root.get_screen("main_window")
    if game_setup_heroes != 3:
        main_window.ids.henchmen_lab.text = "{}".format(randomize_list(henchmen_names,num))
        
    else:
        main_window.ids.henchmen_lab.text = "{} (only 3 cards)".format(randomize_list(henchmen_names,num))

def show_randomized_heroes(num):
    main_window = App.get_running_app().root.get_screen("main_window")
    main_window.ids.heroes_lab.text = "{}".format(randomize_list(heroes_names,num))
                
def show_bystanders(num):
    main_window = App.get_running_app().root.get_screen("main_window")
    main_window.ids.bystanders_lab.text = "{}".format(num)