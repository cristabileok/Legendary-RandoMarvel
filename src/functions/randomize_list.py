import os
import random

from kivy.app import App

from .change_instructions import change_instructions
from .randomize_from_poketset import randomize_from_poketset
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


def randomize_list(type, num):

    change_instructions()

    main_window = App.get_running_app().root.get_screen("main_window")
    poketset_switch = main_window.ids.poketset_switch   


    if not poketset_switch.active:        
        this_list = set()
        while len(this_list) < num:
            item = (type[random.randint(0,len(type)-1)])
            this_list.add(item)

    else:
        game_to_load = open(os.path.join(os.path.dirname(__file__),'../../lists/saved_poketset.txt'), 'r')
        if len(game_to_load.read().splitlines()) != 4:
            this_list = ""

        else:
            this_list = randomize_from_poketset(type,num)

    this_list = sorted(this_list)
    this_list = " / ".join(this_list)
    if type == masterminds_names:
        chance_of_epic = random.randint(1,3)
        if chance_of_epic == 3:
            this_list = "Epic {}".format(this_list)
    return this_list