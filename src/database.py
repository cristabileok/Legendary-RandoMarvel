
import os

schemes_file = open(os.path.join(os.path.dirname(__file__),'../lists/list_schemes.txt'), 'r', encoding="utf8")
schemes_clean = schemes_file.read().replace("\n\n>> ","").replace(">> ","")
schemes_list = schemes_clean.split("///")
schemes_dict_desc = {}
schemes_dict_keys = {}
schemes_names = []
schemes_keywords = []
for scheme in schemes_list:
    titleSCH,descSCH = scheme.split(":::\n")
    if "[-]" in titleSCH :
        nameSCH,keySCHM = titleSCH.split("[-]")
        schemes_dict_keys[nameSCH] = keySCHM.split(" , ")
    else:
        nameSCH = titleSCH
        schemes_dict_keys[nameSCH] = []
    schemes_names.append(nameSCH)
    schemes_dict_desc[nameSCH] = descSCH
    

masterminds_file = open(os.path.join(os.path.dirname(__file__),'../lists/list_masterminds.txt'), 'r')
masterminds_list = masterminds_file.read().splitlines()
masterminds_dict = {}
masterminds_names = []
for line in masterminds_list:
    namesMM,keysMM = line.split(" : ")
    masterminds_names.append(namesMM)
    keysMM_list = keysMM.split(" , ")
    if keysMM_list[0] == "":
        keysMM_list = []
    masterminds_dict[namesMM] = keysMM_list

villains_file = open(os.path.join(os.path.dirname(__file__),'../lists/list_villains.txt'), 'r')
villains_list = villains_file.read().splitlines()
villains_dict = {}
villains_names = []
for line in villains_list:
    namesVi,keysVi = line.split(" : ")
    villains_names.append(namesVi)
    keysVi_list = keysVi.split(" , ")
    if keysVi_list[0] == "":
        keysVi_list = []
    villains_dict[namesVi] = keysVi_list

henchmen_file = open(os.path.join(os.path.dirname(__file__),'../lists/list_henchmen.txt'), 'r')
henchmen_list = henchmen_file.read().splitlines()
henchmen_dict = {}
henchmen_names = []
for line in henchmen_list:
    namesHeN,keysHeN = line.split(" : ")
    henchmen_names.append(namesHeN)
    keysHeN_list = keysHeN.split(" , ")
    if keysHeN_list[0] == "":
        keysHeN_list = []
    henchmen_dict[namesHeN] = keysHeN_list

heroes_file = open(os.path.join(os.path.dirname(__file__),'../lists/list_heroes.txt'), 'r')
heroes_list = heroes_file.read().splitlines()
heroes_dict = {}
heroes_names = []
for line in heroes_list:
    namesHeR,keysHeR = line.split(" : ")
    heroes_names.append(namesHeR)
    keysHeR_list = keysHeR.split(" , ")
    if keysHeR_list[0] == "":
        keysHeR_list = []
    heroes_dict[namesHeR] = keysHeR_list

keywords_file = open(os.path.join(os.path.dirname(__file__),'../lists/list_keywords.txt'), 'r', encoding="utf8")
keywords_clean = keywords_file.read().replace("\n\n>> ","").replace(">> ","")
keywords_list = keywords_clean.split("///")
keywords_dict = {}
keywords_names = set()
for keyword in keywords_list:
    nameKW,descKW = keyword.split(":::\n")
    keywords_dict[nameKW] = descKW
    keywords_names.add(nameKW)