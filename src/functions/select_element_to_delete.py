from kivy.app import App

from ..elements_randomized_dropdown import ElementsRandomizedDropDown
from .reduce import reduce


def select_element_to_delete(category):
        
        main_window = App.get_running_app().root.get_screen("main_window")       

        if category == "scheme":
            button = main_window.ids.reduce_scheme_button
            source = main_window.ids.scheme_lab.text
        elif category == "masterminds":
            button = main_window.ids.reduce_masterminds_button
            source = main_window.ids.mastermind_lab.text
        elif category == "villains":
            button = main_window.ids.reduce_villains_button
            source = main_window.ids.villains_lab.text
        elif category == "henchmen":
            button = main_window.ids.reduce_henchmen_button
            source = main_window.ids.henchmen_lab.text
        elif category == "heroes":
            button = main_window.ids.reduce_heroes_button
            source = main_window.ids.heroes_lab.text
        else:
             pass
        
        if source == "":
            pass

        if "/" not in source:
            reduce(category)

        else:
            elements_randomized_dropdown = ElementsRandomizedDropDown(category,source)
            elements_randomized_dropdown.category = category            
            elements_randomized_dropdown.open(button)