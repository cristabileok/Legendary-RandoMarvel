import random

from .change_instructions import change_instructions
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

def randomize_list(type, num):

    change_instructions()

    list = set()
    while len(list) < num:
        list.add(type[random.randint(0,len(type)-1)])
    list = sorted(list)
    list = " / ".join(list)
    if type == masterminds_names:
        chance_of_epic = random.randint(1,3)
        if chance_of_epic == 3:
            list = "Epic {}".format(list)
    return list