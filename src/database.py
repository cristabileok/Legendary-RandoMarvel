import json
import os

schemes_file = open(os.path.join(os.path.dirname(__file__),'../lists/schemes.json'), encoding='utf-8')
schemes_data = json.load(schemes_file)
schemes_dict_keys = {}
schemes_dict_desc = {}

schemes_names = []

for scheme in schemes_data:
    nameScheme, keyScheme, descScheme = scheme["name"], scheme["keywords"], scheme["description"]

    schemes_dict_keys[nameScheme] = keyScheme
    
    schemes_dict_desc[nameScheme] = descScheme    

    schemes_names.append(nameScheme)    

masterminds_file = open(os.path.join(os.path.dirname(__file__),'../lists/masterminds.json'), encoding='utf-8')
masterminds_data = json.load(masterminds_file)

masterminds_to_keywords = {}
masterminds_to_villains = {}
masterminds_to_henchmen = {}
masterminds_names = []

for mastermind in masterminds_data:
    nameMastermind, keyMastermind, villainsMastermind, henchmenMastermind = mastermind["name"], mastermind["keywords"], mastermind["villains_groups"], mastermind["henchmen_groups"]
    if keyMastermind[0] == "":
        keyMastermind = []
    masterminds_to_keywords[nameMastermind] = keyMastermind
    masterminds_to_villains[nameMastermind] = villainsMastermind
    masterminds_to_henchmen[nameMastermind] = henchmenMastermind
    masterminds_names.append(nameMastermind)

villains_file = open(os.path.join(os.path.dirname(__file__),'../lists/villains.json'), encoding='utf-8')
villains_data = json.load(villains_file)
villains_dict = {}
villains_names = []
for villain in villains_data:
    nameVillain,keyVillain = villain["name"],villain["keywords"]
    if keyVillain[0] == "":
        keyVillain = []
    villains_dict[nameVillain] = keyVillain
    villains_names.append(nameVillain)

henchmen_file = open(os.path.join(os.path.dirname(__file__),'../lists/henchmen.json'), encoding='utf-8')
henchmen_data = json.load(henchmen_file)
henchmen_dict = {}
henchmen_names = []
for henchmen in henchmen_data:
    nameHenchman,keyHenchman = henchmen["name"],henchmen["keywords"]
    if keyHenchman[0] == "":
        keyHenchman = []
    henchmen_dict[nameHenchman] = keyHenchman
    henchmen_names.append(nameHenchman)

heroes_file = open(os.path.join(os.path.dirname(__file__),'../lists/heroes.json'), encoding='utf-8')
heroes_data = json.load(heroes_file)
heroes_dict = {}
heroes_names = []
for hero in heroes_data:
    nameHeroe,keyHeroe = hero["name"],hero["keywords"]
    if keyHeroe[0] == "":
        keyHeroe = []
    heroes_dict[nameHeroe] = keyHeroe
    heroes_names.append(nameHeroe)

keywords_file = open(os.path.join(os.path.dirname(__file__),'../lists/keywords.json'), encoding='utf-8')
keywords_data = json.load(keywords_file)
keywords_dict = {}
keywords_names = set()
for keyword in keywords_data:
    nameKW,descKW = keyword["name"],keyword["description"]
    keywords_dict[nameKW] = descKW
    keywords_names.add(nameKW)