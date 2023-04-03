from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from .label_scroll import Label_Scroll

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

from .functions.create_keywords_list import create_keywords_list
from .functions.create_this_scheme_description import create_this_scheme_description
from .functions.search_input import search_input
from .functions.load_and_save import load_game, save_game
#from .functions.set_to_game import set_to_game

number_of_villains = 1
number_of_henchmen = 1
number_of_heroes = 1

class Main_Window(Screen):
    
    def set_player_1(self):
        global number_of_villains
        global number_of_henchmen
        global number_of_heroes
        number_of_villains = 1
        number_of_henchmen = 1
        number_of_heroes = 3

    def set_player_2(self):
        global number_of_villains
        global number_of_henchmen
        global number_of_heroes
        number_of_villains = 1
        number_of_henchmen = 1
        number_of_heroes = 5

    def set_player_3(self):
        global number_of_villains
        global number_of_henchmen
        global number_of_heroes
        number_of_villains = 2
        number_of_henchmen = 1
        number_of_heroes = 5

    def set_player_4(self):
        global number_of_villains
        global number_of_henchmen
        global number_of_heroes
        number_of_villains = 2
        number_of_henchmen = 2
        number_of_heroes = 5

    
    def randomize_list(self, type, num):
        self.change_instructions()
                
        list = set()
        while len(list) < num:
            list.add(type[random.randint(0,len(type)-1)])
        list = " / ".join(list)
        if type == masterminds_names:
            chance_of_epic = random.randint(1,3)
            if chance_of_epic == 3:
                list = "Epic {}".format(list)
        return list

    def show_randomized_schemes(self,num):
        self.ids.scheme_lab.text = "{}".format(self.randomize_list(schemes_names,num))
        while "|" in self.ids.scheme_lab.text:
            self.ids.scheme_lab.text = "{}".format(self.randomize_list(schemes_names,num))
        
    def show_randomized_mastermind(self, num):
        self.ids.mastermind_lab.text = "{}".format(self.randomize_list(masterminds_names,num))

    def show_randomized_villains(self, num):
        self.ids.villains_lab.text = "{}".format(self.randomize_list(villains_names,num))

    def show_randomized_henchmen(self, num):
        if number_of_heroes != 3:
            self.ids.henchmen_lab.text = "{}".format(self.randomize_list(henchmen_names,num))
            
        else:
            self.ids.henchmen_lab.text = "{} (only 3 cards)".format(self.randomize_list(henchmen_names,num))

    def show_randomized_heroes(self,num):
        self.ids.heroes_lab.text = "{}".format(self.randomize_list(heroes_names,num))
                    
    def show_bystanders(self,num):
        self.ids.bystanders_lab.text = "{}".format(num)
 

    def show_1_scheme(self):
        self.show_randomized_schemes(1)

    def show_1_mastermind(self):
        self.show_randomized_mastermind(1)

    def show_1_villain(self):
        self.show_randomized_villains(number_of_villains)

    def show_1_henchman(self):
        self.show_randomized_henchmen(number_of_henchmen)

    def show_1_heroe(self):
        self.show_randomized_heroes(number_of_heroes)

    def randomize_1_player(self):
        self.set_player_1()
        self.show_randomized_schemes(1)
        self.show_randomized_mastermind(1)
        self.show_randomized_villains(number_of_villains)
        self.show_randomized_henchmen(number_of_henchmen)
        self.show_randomized_heroes(number_of_heroes)
        self.show_bystanders(1)

    def randomize_2_player(self):
        self.set_player_2()
        self.show_randomized_schemes(1)
        self.show_randomized_mastermind(1)
        self.show_randomized_villains(number_of_villains)
        self.show_randomized_henchmen(number_of_henchmen)
        self.show_randomized_heroes(number_of_heroes)
        self.show_bystanders(2)

    def randomize_3_player(self):
        self.set_player_3()
        self.show_randomized_schemes(1)
        self.show_randomized_mastermind(1)
        self.show_randomized_villains(number_of_villains)
        self.show_randomized_henchmen(number_of_henchmen)
        self.show_randomized_heroes(number_of_heroes)
        self.show_bystanders(8)

    def randomize_4_player(self):
        self.set_player_4()
        self.show_randomized_schemes(1)
        self.show_randomized_mastermind(1)
        self.show_randomized_villains(number_of_villains)
        self.show_randomized_henchmen(number_of_henchmen)
        self.show_randomized_heroes(number_of_heroes)
        self.show_bystanders(8)
        
    def add_random_mastermind(self):
        self.add_random_element(masterminds_names)
        
    def add_random_villain(self):
        self.add_random_element(villains_names)
        
    def add_random_henchman(self):
        self.add_random_element(henchmen_names)
        
    def add_random_heroe(self):
        self.add_random_element(heroes_names)
        
    def add_random_element(self,type):
        if type == masterminds_names:
            old_text = self.ids.mastermind_lab.text
        elif type == villains_names:
            old_text = self.ids.villains_lab.text
        elif type == henchmen_names:
            old_text = self.ids.henchmen_lab.text
        elif type == heroes_names:
            old_text = self.ids.heroes_lab.text
            
        if old_text == "":
            if type == masterminds_names:
                self.show_1_mastermind()
            elif type == villains_names:
                self.show_1_villain()
            elif type == henchmen_names:
                self.show_1_henchman()
            elif type == heroes_names:
                self.show_1_heroe()
                
        else:        
            old_set = set(old_text.split(" / "))
            
            old_length = len(old_set)
            
            while len(old_set) == old_length and len(old_set) < len(type):
                old_set.add(str(self.randomize_list(type,1)))
                
            new_text = " / ".join(old_set)
            
            if type == masterminds_names:
                self.ids.mastermind_lab.text = "{}".format(new_text)
            elif type == villains_names:
                self.ids.villains_lab.text = "{}".format(new_text)
            elif type == henchmen_names:
                self.ids.henchmen_lab.text = "{}".format(new_text)
            elif type == heroes_names:
                self.ids.heroes_lab.text = "{}".format(new_text)
                

    def reduce_scheme(self):
        old_text = self.ids.scheme_lab.text
        list = old_text.split(" / ")
        _ = list.pop()
        new_text = " / ".join(list)
        self.ids.scheme_lab.text = "{}".format(new_text)
        
    def reduce_mastermind(self):
        old_text = self.ids.mastermind_lab.text
        list = old_text.split(" / ")
        _ = list.pop()
        new_text = " / ".join(list)
        self.ids.mastermind_lab.text = "{}".format(new_text)
        
    def reduce_villains(self):
        old_text = self.ids.villains_lab.text
        list = old_text.split(" / ")
        _ = list.pop()
        new_text = " / ".join(list)
        self.ids.villains_lab.text = "{}".format(new_text)
        
    def reduce_henchmen(self):
        old_text = self.ids.henchmen_lab.text
        list = old_text.split(" / ")
        _ = list.pop()
        new_text = " / ".join(list)
        self.ids.henchmen_lab.text = "{}".format(new_text)
        
    def reduce_heroes(self):
        old_text = self.ids.heroes_lab.text
        list = old_text.split(" / ")
        _ = list.pop()
        new_text = " / ".join(list)
        self.ids.heroes_lab.text = "{}".format(new_text)
        
               
    def reset(self):
        global number_of_villains
        global number_of_henchmen
        global number_of_heroes
        number_of_villains = 1
        number_of_henchmen = 1
        number_of_heroes = 1        

        self.ids.instructions.text="Select Number of Players\nor Categories to be Randomized"
        self.ids.scheme_lab.text=''
        self.ids.mastermind_lab.text=''
        self.ids.villains_lab.text=''
        self.ids.henchmen_lab.text=''
        self.ids.heroes_lab.text=''
        self.ids.bystanders_lab.text=''

    def change_instructions(self):
        self.ids.instructions.text="Press on the Results\nto see Descriptions or Keywords"
    
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
        carrier_text = self.ids.mastermind_lab.text
        dict = masterminds_dict
        title = "Mastermind"
        self.show_keywords_list(carrier_text,dict,title)

    def show_villains_keywords(self):
        carrier_text = self.ids.villains_lab.text
        dict = villains_dict
        title = "Villains"
        self.show_keywords_list(carrier_text,dict,title)

    def show_henchmen_keywords(self):
        carrier_text = self.ids.henchmen_lab.text
        dict = henchmen_dict
        title = "Henchmen"
        self.show_keywords_list(carrier_text,dict,title)

    def show_heroes_keywords(self):
        carrier_text = self.ids.heroes_lab.text
        dict = heroes_dict
        title = "Heroes"
        self.show_keywords_list(carrier_text,dict,title)


    def create_this_scheme_description(self,scheme):        
        create_this_scheme_description(self,scheme)
                
    def go_to_scheme_description(self):
        scheme = self.ids.scheme_lab.text
        self.create_this_scheme_description(scheme)

    def search_input(self):
        search_input(self)
        
    def go_to_search(self):
        app = App.get_running_app()
        app.root.get_screen("main_window").manager.transition.direction = "left"
        app.root.get_screen("main_window").manager.current = "search_window"
        app.root.get_screen("search_window").ids.textinput.focus=True

    def save_game(self):
        save_game(self,number_of_villains,number_of_henchmen,number_of_heroes)

    def load_game(self):
        global number_of_villains
        global number_of_henchmen
        global number_of_heroes
        number_of_villains,number_of_henchmen,number_of_heroes = load_game(self)