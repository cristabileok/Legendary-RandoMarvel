from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

from .functions.load_and_save import save_game

class SaveGameDropdown(DropDown):
    def __init__(self, number_of_villains, number_of_henchmen, number_of_heroes, **kwargs):
        super(SaveGameDropdown,self).__init__(**kwargs)
        self.number_of_villains = number_of_villains
        self.number_of_henchmen = number_of_henchmen
        self.number_of_heroes = number_of_heroes
        
    def save_game(self):
        save_game(self.number_of_villains, self.number_of_henchmen, self.number_of_heroes)

    def clear_dropdown(self):
                self.dismiss()               
