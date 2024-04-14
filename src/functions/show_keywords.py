from kivy.app import App

from .show_keywords_list import show_keywords_list

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


def show_masterminds_keywords(btn):
    main_window = App.get_running_app().root.get_screen("main_window")
    carrier_text = main_window.ids.mastermind_lab.text
    if carrier_text == "":
        pass
    else:
        dict = masterminds_to_keywords
        title = "Mastermind"
        show_keywords_list(btn,carrier_text,dict,title)

def show_villains_keywords(btn):
    main_window = App.get_running_app().root.get_screen("main_window")
    carrier_text = main_window.ids.villains_lab.text
    if carrier_text == "":
        pass
    else:
        dict = villains_dict
        title = "Villains"
        show_keywords_list(btn,carrier_text,dict,title)

def show_henchmen_keywords(btn):
    main_window = App.get_running_app().root.get_screen("main_window")
    carrier_text = main_window.ids.henchmen_lab.text
    if carrier_text == "":
        pass
    else:
        dict = henchmen_dict
        title = "Henchmen"
        show_keywords_list(btn,carrier_text,dict,title)

def show_heroes_keywords(btn):
    main_window = App.get_running_app().root.get_screen("main_window")
    carrier_text = main_window.ids.heroes_lab.text
    if carrier_text == "":
        pass
    else:
        dict = heroes_dict
        title = "Heroes"
        show_keywords_list(btn,carrier_text,dict,title)