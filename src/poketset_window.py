from kivy.app import App
from kivy.uix.screenmanager import Screen

from .main_window import Main_Window

from .functions.add_random_element_to_poketset import add_random_element_to_poketset
from .functions.confirm_save_poketset import confirm_save_poketset
from .functions.go_to_search import go_to_search
from .functions.poketset_load_and_save import load_poketset
from .functions.poketset_reset import reset_poketset
from .functions.select_element_to_delete_poketset import select_element_to_delete_poketset
from .functions.show_poketset_elements import show_poketset_randomized_henchmen, show_poketset_randomized_heroes, show_poketset_randomized_mastermind, show_poketset_randomized_villains
from .functions.adjust_poketset_to_input import adjust_poketset_to_henchman, adjust_poketset_to_mastermind, adjust_poketset_to_villain

from .database import (
    masterminds_names,
    villains_names,
    henchmen_names,
    heroes_names,
)

class PoketSet_Window(Screen):
    
    def go_to_search(self,btn):
        go_to_search(btn)
    
    def change_poketset_masterminds(self):
        poketset_window = App.get_running_app().root.get_screen("poketset_window")
        masterminds_text = poketset_window.ids.poketset_masterminds.text
        if not masterminds_text == "":
            masterminds_list = masterminds_text.split(" / ")
            masterminds_number = len(masterminds_list)
            show_poketset_randomized_mastermind(masterminds_number)
            adjust_poketset_to_mastermind(masterminds_text.replace("Epic ",""))



    def add_random_mastermind_to_poketset(self):
        add_random_element_to_poketset(masterminds_names)

    def select_masterminds_to_delete_poketset(self):
        select_element_to_delete_poketset("masterminds_poketset")

    def change_poketset_villains(self):
        poketset_window = App.get_running_app().root.get_screen("poketset_window")
        villains_text = poketset_window.ids.poketset_villains.text
        if not villains_text == "":
            villains_list = villains_text.split(" / ")
            villains_number = len(villains_list)
            show_poketset_randomized_villains(villains_number)
            adjust_poketset_to_villain(villains_text)


    def add_random_villain_to_poketset(self):
        add_random_element_to_poketset(villains_names)

    def select_villains_to_delete_poketset(self):
        select_element_to_delete_poketset("villains_poketset")

    def change_poketset_henchmen(self):
        poketset_window = App.get_running_app().root.get_screen("poketset_window")
        henchmen_text = poketset_window.ids.poketset_henchmen.text
        if not henchmen_text == "":
            henchmen_list = henchmen_text.split(" / ")
            henchmen_number = len(henchmen_list)
            show_poketset_randomized_henchmen(henchmen_number)
            adjust_poketset_to_henchman(henchmen_text)


    def add_random_henchman_to_poketset(self):
        add_random_element_to_poketset(henchmen_names)

    def select_henchmen_to_delete_poketset(self):
        select_element_to_delete_poketset("henchmen_poketset")

    def change_poketset_heroes(self):
        poketset_window = App.get_running_app().root.get_screen("poketset_window")
        heroes_text = poketset_window.ids.poketset_heroes.text
        if not heroes_text == "":
            heroes_list = heroes_text.split(" / ")
            heroes_number = len(heroes_list)
            show_poketset_randomized_heroes(heroes_number)

    def add_random_heroe_to_poketset(self):
        add_random_element_to_poketset(heroes_names)

    def select_heroes_to_delete_poketset(self):
        select_element_to_delete_poketset("heroes_poketset")

    def create_poketset(self):
        poketset_window = App.get_running_app().root.get_screen("poketset_window")
        enemies_number = int(poketset_window.ids.poketset_number_enemies_input.text)
        heroes_number = int(poketset_window.ids.poketset_number_heroes_input.text)

        reset_poketset()

        show_poketset_randomized_mastermind(enemies_number-2)
        add_random_element_to_poketset(villains_names)
        add_random_element_to_poketset(henchmen_names)
        show_poketset_randomized_heroes(heroes_number)


    def confirm_save_poketset(self):
        confirm_save_poketset()

    def load_poketset(self):
        load_poketset()

    def reset_poketset(self):
        reset_poketset()
