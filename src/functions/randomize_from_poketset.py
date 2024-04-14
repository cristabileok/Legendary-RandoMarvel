import os
import random

from kivy.app import App

from ..database import (
    schemes_names,
    masterminds_names,
    villains_names,
    henchmen_names,
    heroes_names,
)

def randomize_from_poketset(type,num):
    
    poketset = open(os.path.join(os.path.dirname(__file__),'../../lists/saved_poketset.txt'), 'r')
    poketset_masterminds, poketset_villains, poketset_henchmen, poketset_heroes = poketset.read().splitlines()
    poketset_masterminds = poketset_masterminds.split(" / ")
    poketset_villains = poketset_villains.split(" / ")
    poketset_henchmen = poketset_henchmen.split(" / ")
    poketset_heroes = poketset_heroes.split(" / ")

    this_list = set()

        
    if type == masterminds_names:
        while len(this_list) < num and len(this_list) < len(poketset_masterminds):
            item = (poketset_masterminds[random.randint(0,len(poketset_masterminds)-1)])
            this_list.add(item)

    elif type == villains_names:
        while len(this_list) < num and len(this_list) < len(poketset_villains):
            item = (poketset_villains[random.randint(0,len(poketset_villains)-1)])
            this_list.add(item)

    elif type == henchmen_names:
        while len(this_list) < num and len(this_list) < len(poketset_henchmen):
            item = (poketset_henchmen[random.randint(0,len(poketset_henchmen)-1)])
            this_list.add(item)

    elif type == heroes_names: 
        
        while len(this_list) < num and len(this_list) < len(poketset_heroes):
            item = (poketset_heroes[random.randint(0,len(poketset_heroes)-1)])
            this_list.add(item)
            

    else:
        while len(this_list) < num and len(this_list) < len(schemes_names):
            item = (type[random.randint(0,len(type)-1)])
            this_list.add(item)
 
    return this_list