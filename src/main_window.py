from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from .label_scroll import Label_Scroll
from .player_number_dropdown import PlayerNumberDropDown
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
from .functions.create_keywords_list import create_keywords_list
from .functions.create_this_scheme_description import create_this_scheme_description
from .functions.load_and_save import load_game, save_game
from .functions.go_to_search import go_to_search
from .functions.reduce import reduce_henchmen, reduce_heroes, reduce_mastermind, reduce_scheme, reduce_villains
from .functions.show_elements import show_bystanders, show_randomized_henchmen, show_randomized_heroes, show_randomized_mastermind, show_randomized_schemes, show_randomized_villains
from .functions.randomize_n_player import randomize_1_player, randomize_2_player, randomize_3_player, randomize_4_player

game_setup = SetupNumbers()

class Main_Window(Screen):

    def select_player_number(self):
        player_number_dropdown = PlayerNumberDropDown()
        main_window = App.get_running_app().root.get_screen("main_window")
        player_number_dropdown.open(main_window.ids.select_number_players_button)
    
        
    def show_randomized_schemes(self,num):
        show_randomized_schemes(num)
        
    def show_randomized_mastermind(self,num):
        show_randomized_mastermind(num)

    def show_randomized_villains(self,num):
        show_randomized_villains(num)

    def show_randomized_henchmen(self,num):
        show_randomized_henchmen(num,game_setup.number_of_heroes)

    def show_randomized_heroes(self,num):
        show_randomized_heroes(num)

    def show_bystanders(self,num):
        show_bystanders(num)
        
    

    def show_1_scheme(self):
        self.show_randomized_schemes(1)

    def show_1_mastermind(self):
        self.show_randomized_mastermind(1)

    def show_1_villain(self):
        self.show_randomized_villains(game_setup.number_of_villains)

    def show_1_henchman(self):
        self.show_randomized_henchmen(game_setup.number_of_henchmen)

    def show_1_heroe(self):
        self.show_randomized_heroes(game_setup.number_of_heroes)

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
        
    
    def reduce_scheme(self):
        reduce_scheme()

    def reduce_mastermind(self):
        reduce_mastermind()
    
    def reduce_villains(self):
        reduce_villains()

    def reduce_henchmen(self):
        reduce_henchmen()

    def reduce_heroes(self):
        reduce_heroes()
    
        
               
    def reset(self):
        game_setup.number_of_villains = 1
        game_setup.number_of_henchmen = 1
        game_setup.number_of_heroes = 1
 
        main_window = App.get_running_app().root.get_screen("main_window")
        main_window.ids.instructions.text="Select Number of Players\nor Categories to be Randomized"
        main_window.ids.scheme_lab.text=''
        main_window.ids.mastermind_lab.text=''
        main_window.ids.villains_lab.text=''
        main_window.ids.henchmen_lab.text=''
        main_window.ids.heroes_lab.text=''
        main_window.ids.bystanders_lab.text=''

    #def change_instructions(self):
    #    main_window = App.get_running_app().root.get_screen("main_window")
    #    main_window.ids.instructions.text="Press on the Results\nto see Descriptions or Keywords"
    
    def show_keywords_list(self,carrier,dict,title):
        self.create_keywords_list(carrier,dict,title)
        self.go_to_keywords_description()
    
    def create_keywords_list(self,carrier,dict,title):        
        create_keywords_list(self,carrier,dict,title)
        
    def go_to_keywords_description(self):
        app = App.get_running_app()
        app.root.get_screen("main_window").manager.transition.direction = "left"
        app.root.get_screen("main_window").manager.current = "keywords_window"
            
    def show_masterminds_keywords(self):
        main_window = App.get_running_app().root.get_screen("main_window")
        carrier_text = main_window.ids.mastermind_lab.text
        if carrier_text == "":
            pass
        else:
            dict = masterminds_dict
            title = "Mastermind"
            self.show_keywords_list(carrier_text,dict,title)

    def show_villains_keywords(self):
        main_window = App.get_running_app().root.get_screen("main_window")
        carrier_text = main_window.ids.villains_lab.text
        if carrier_text == "":
            pass
        else:
            dict = villains_dict
            title = "Villains"
            self.show_keywords_list(carrier_text,dict,title)

    def show_henchmen_keywords(self):
        main_window = App.get_running_app().root.get_screen("main_window")
        carrier_text = main_window.ids.henchmen_lab.text
        if carrier_text == "":
            pass
        else:
            dict = henchmen_dict
            title = "Henchmen"
            self.show_keywords_list(carrier_text,dict,title)

    def show_heroes_keywords(self):
        main_window = App.get_running_app().root.get_screen("main_window")
        carrier_text = main_window.ids.heroes_lab.text
        if carrier_text == "":
            pass
        else:
            dict = heroes_dict
            title = "Heroes"
            self.show_keywords_list(carrier_text,dict,title)


    def create_this_scheme_description(self,scheme):        
        create_this_scheme_description(self,scheme)
                
    def go_to_scheme_description(self):
        main_window = App.get_running_app().root.get_screen("main_window")
        scheme = main_window.ids.scheme_lab.text
        self.create_this_scheme_description(scheme)

    def go_to_search(self):
        go_to_search()

    def save_game(self):
        save_game(game_setup.number_of_villains,game_setup.number_of_henchmen,game_setup.number_of_heroes)

    def load_game(self):
        game_setup.number_of_villains,game_setup.number_of_henchmen,game_setup.number_of_heroes = load_game()
        change_instructions()