from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from .label_scroll import Label_Scroll
from .player_number_dropdown import PlayerNumberDropDown
from .elements_randomized_dropdown import ElementsRandomizedDropDown
from .setup_numbers import SetupNumbers

import os
import random


from .database import (
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

from .functions.add_random_element import add_random_element
from .functions.change_instructions import change_instructions
from .functions.go_to_keywords_description import go_to_keywords_description
from .functions.go_to_scheme_description import go_to_scheme_description
from .functions.go_to_search import go_to_search
from .functions.load_and_save import load_game, save_game
from .functions.randomize_n_player import randomize_1_player, randomize_2_player, randomize_3_player, randomize_4_player
from .functions.reset import reset
from .functions.select_element_to_delete import select_element_to_delete
from .functions.select_player_number import select_player_number
from .functions.show_elements import show_bystanders, show_randomized_henchmen, show_randomized_heroes, show_randomized_mastermind, show_randomized_schemes, show_randomized_villains
from .functions.show_keywords import show_henchmen_keywords, show_heroes_keywords, show_masterminds_keywords, show_villains_keywords


game_setup = SetupNumbers()

class Main_Window(Screen):

    def select_player_number(self):
        select_player_number(game_setup)

    
    def show_1_scheme(self):
        show_randomized_schemes(1)

    def show_1_mastermind(self):
        show_randomized_mastermind(1)

    def show_1_villain(self):
        show_randomized_villains(game_setup.number_of_villains)

    def show_1_henchman(self):
        show_randomized_henchmen(game_setup.number_of_henchmen,game_setup.number_of_heroes)

    def show_1_heroe(self):
        show_randomized_heroes(game_setup.number_of_heroes)


    def randomize_1_player(self):
        randomize_1_player(game_setup)

    def randomize_2_player(self):
        randomize_2_player(game_setup)

    def randomize_3_player(self):
        randomize_3_player(game_setup)

    def randomize_4_player(self):
        randomize_4_player(game_setup)
                
        
    def add_random_mastermind(self):
        add_random_element(masterminds_names)
        
    def add_random_villain(self):
        add_random_element(villains_names)
        
    def add_random_henchman(self):
        add_random_element(henchmen_names,game_setup.number_of_heroes)
        
    def add_random_heroe(self):
        add_random_element(heroes_names)

    def select_scheme_to_delete(self):
        select_element_to_delete("scheme")

    def select_masterminds_to_delete(self):
        select_element_to_delete("masterminds")

    def select_villains_to_delete(self):
        select_element_to_delete("villains")

    def select_henchmen_to_delete(self):
        select_element_to_delete("henchmen")

    def select_heroes_to_delete(self):
        select_element_to_delete("heroes")
   
     
    def reset(self):
        reset(game_setup)
        
         
    def show_masterminds_keywords(self):
        show_masterminds_keywords()

    def show_villains_keywords(self):
        show_villains_keywords()

    def show_henchmen_keywords(self):
        show_henchmen_keywords()

    def show_heroes_keywords(self):
        show_heroes_keywords()

                
    def go_to_scheme_description(self):
        go_to_scheme_description()

    def go_to_keywords_description(self):
        go_to_keywords_description()

    def go_to_search(self):
        go_to_search()


    def save_game(self):
        save_game(game_setup.number_of_villains,game_setup.number_of_henchmen,game_setup.number_of_heroes)

    def load_game(self):
        game_setup.number_of_villains,game_setup.number_of_henchmen,game_setup.number_of_heroes = load_game()
        change_instructions()