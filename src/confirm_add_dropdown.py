from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from .functions.poketset_load_and_save import save_poketset
from .list_item_button import List_Item_Button

class ConfirmAddDropdown(DropDown):
    def __init__(self, trigger,category, **kwargs):
        super(ConfirmAddDropdown,self).__init__(**kwargs)
        self.trigger = trigger
        self.category = category

        box = BoxLayout()
        box.orientation = 'horizontal'
        box.size_hint_y = None
        box.spacing = 5
        box.paddint = 5

        self.add_widget(box) 


        add_to_game_button = List_Item_Button()
        add_to_game_button.text ="Add to Game"
        add_to_game_button.background_color = (0.1,0.1,0.1,1)                

        add_to_game_button.bind(on_release=lambda instance, trigger=trigger, category=category: instance.add_element_to_game(instance, trigger, category))

        add_to_game_button.bind(on_release=lambda instance: instance.remove_parent_dropdown(instance))


        box.add_widget(add_to_game_button)

        add_to_poketset_button = List_Item_Button()
        add_to_poketset_button.text = "Add to Poket Set"
        add_to_poketset_button.background_color = (0.1,0.1,0.1,1)        

        add_to_poketset_button.bind(on_release=lambda instance, trigger=trigger, category=category: instance.add_element_to_poketset(instance, trigger, category))


        add_to_poketset_button.bind(on_release=lambda instance: instance.remove_parent_dropdown(instance))

        box.add_widget(add_to_poketset_button)
        

    def clear_dropdown(self):
        self.dismiss()               
