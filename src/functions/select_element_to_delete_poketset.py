from kivy.app import App

from ..elements_randomized_dropdown import ElementsRandomizedDropDown
from .reduce import reduce


def select_element_to_delete_poketset(category):
        
        poketset_window = App.get_running_app().root.get_screen("poketset_window")       

        match category:
            case "masterminds_poketset":
                button = poketset_window.ids.reduce_masterminds_poketset_button
                source = poketset_window.ids.poketset_masterminds.text
            case "villains_poketset":
                button = poketset_window.ids.reduce_villains_poketset_button
                source = poketset_window.ids.poketset_villains.text
            case "henchmen_poketset":
                button = poketset_window.ids.reduce_henchmen_poketset_button
                source = poketset_window.ids.poketset_henchmen.text
            case "heroes_poketset":
                button = poketset_window.ids.reduce_heroes_poketset_button
                source = poketset_window.ids.poketset_heroes.text
                
        if source == "":
            pass

        if "/" not in source:
            reduce(category)

        else:
            elements_randomized_dropdown = ElementsRandomizedDropDown(category,source)
            elements_randomized_dropdown.category = category            
            elements_randomized_dropdown.open(button)