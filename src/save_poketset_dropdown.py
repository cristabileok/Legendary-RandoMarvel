from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

from .functions.poketset_load_and_save import save_poketset

class SavePoketsetDropdown(DropDown):
    def __init__(self, **kwargs):
        super(SavePoketsetDropdown,self).__init__(**kwargs)
        
        
    def save_poketset(self):
        save_poketset()

    def clear_dropdown(self):
        self.dismiss()               
