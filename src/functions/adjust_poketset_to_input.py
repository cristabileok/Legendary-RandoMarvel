import os

from kivy.app import App

from ..database import (
    masterminds_names,
    villains_names,
    henchmen_names,
    masterminds_to_villains,
    masterminds_to_henchmen
)


def adjust_poketset_to_mastermind(input):
    
    poketset_window = App.get_running_app().root.get_screen("poketset_window")
    masterminds_text = poketset_window.ids.poketset_masterminds.text
    villains_text = poketset_window.ids.poketset_villains.text
    henchmen_text = poketset_window.ids.poketset_henchmen.text
    
    clean_input_list = input.replace("Epic ","").split(" / ")

    if masterminds_text == "":
        masterminds_list = []
    else:
        masterminds_list = masterminds_text.replace("Epic ","").split(" / ")
    masterminds_set = set(masterminds_list)

    if villains_text == "":
        villains_list = []
    else:
        villains_list = villains_text.split(" / ")
    villains_set = set(villains_list)

    if henchmen_text == "":
        henchmen_list = []
    else:
        henchmen_list = henchmen_text.split(" / ")
    henchmen_set = set(henchmen_list)

    for element in clean_input_list:
                
        if element in masterminds_list:                        
            villains_set.update(set(masterminds_to_villains[element]))
            henchmen_set.update(set(masterminds_to_henchmen[element]))         


        if element not in masterminds_list:            
            villains_set = {i for i in villains_list if i not in masterminds_to_villains[element]}
            henchmen_set = {i for i in henchmen_list if i not in masterminds_to_henchmen[element]}

        else:
            pass             

        masterminds_list = sorted(masterminds_set)
        villains_list = sorted(villains_set)
        henchmen_list = sorted(henchmen_set)

    poketset_window.ids.poketset_masterminds.text = " / ".join(masterminds_list)   
    poketset_window.ids.poketset_villains.text = " / ".join(villains_list)
    poketset_window.ids.poketset_henchmen.text = " / ".join(henchmen_list)


def adjust_poketset_to_villain(input):

    poketset_window = App.get_running_app().root.get_screen("poketset_window")
    masterminds_text = poketset_window.ids.poketset_masterminds.text
    villains_text = poketset_window.ids.poketset_villains.text

    clean_input_list = input.replace("Epic ","").split(" / ")    

    if masterminds_text == "":
        masterminds_list = []
    else:
        masterminds_list = masterminds_text.replace("Epic ","").split(" / ")
    masterminds_set = set(masterminds_list)
        

    if villains_text == "":
        villains_list = []
    else:
        villains_list = villains_text.split(" / ")
    villains_set = set(villains_list)    


    for element in clean_input_list:               
        
        this_villain_mastermind = {key for key in masterminds_to_villains if element in masterminds_to_villains[key]}
        
        if element in villains_list:

            masterminds_set.update(this_villain_mastermind)            

        if element not in villains_list:

            masterminds_set = {i for i in masterminds_list if i not in this_villain_mastermind}
            

        else:
            pass

        masterminds_list = sorted(masterminds_set)
        villains_list = sorted(villains_set)        

    poketset_window.ids.poketset_masterminds.text = " / ".join(masterminds_list)   
    poketset_window.ids.poketset_villains.text = " / ".join(villains_list)    

def adjust_poketset_to_henchman(input):

    poketset_window = App.get_running_app().root.get_screen("poketset_window")
    masterminds_text = poketset_window.ids.poketset_masterminds.text    
    henchmen_text = poketset_window.ids.poketset_henchmen.text

    clean_input_list = input.replace("Epic ","").split(" / ")

    if masterminds_text == "":
        masterminds_list = []
    else:
        masterminds_list = masterminds_text.replace("Epic ","").split(" / ")
    masterminds_set = set(masterminds_list)

    if henchmen_text == "":
        henchmen_list = []
    else:
        henchmen_list = henchmen_text.split(" / ")
    henchmen_set = set(henchmen_list)

    for element in clean_input_list:

        this_henchman_mastermind = {i for i in masterminds_to_henchmen if element in masterminds_to_henchmen[i]}

        if element in henchmen_list:

                masterminds_set.update(this_henchman_mastermind)

        if element not in henchmen_list:

            masterminds_set = {i for i in masterminds_list if i not in this_henchman_mastermind}
        
        else:
            pass

        masterminds_list = sorted(masterminds_set)
        henchmen_list = sorted(henchmen_set)

    poketset_window.ids.poketset_masterminds.text = " / ".join(masterminds_list)   
    poketset_window.ids.poketset_henchmen.text = " / ".join(henchmen_list)


    
