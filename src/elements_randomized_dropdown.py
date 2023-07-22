from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label

from .setup_numbers import SetupNumbers
from .list_item_button import List_Item_Button

class ElementsRandomizedDropDown(DropDown):
    def __init__(self, category, source,**kwargs):
        super(ElementsRandomizedDropDown,self).__init__(**kwargs)
        main_window = App.get_running_app().root.get_screen("main_window")
        
        box = BoxLayout(orientation='vertical')
        box.orientation = 'vertical'
        box.size_hint_y = None
        box.spacing = 5
        box.padding = 5
        self.add_widget(box)

        label = Label()
        label.size_hint_y = None
        label.text = f"Which {category} to remove?"
                
        label.background_color = (0,0,0,1)
        
        box.height = box.height + 10
        box.add_widget(label)

        source_list = source.split(" / ")

        dict_of_buttons = {}


        for item in source_list:
            dict_of_buttons[item] = List_Item_Button()
            dict_of_buttons[item].text = "{}".format(item)
            dict_of_buttons[item].size_hint_y = None
            dict_of_buttons[item].height = 50
            dict_of_buttons[item].auto_width = True

            match category:
                case "scheme":
                    dict_of_buttons[item].background_color = (45/255, 145/255, 73/255, 1)                
                case "masterminds":
                    dict_of_buttons[item].background_color = (119/255.0, 50/255.0, 168/255.0,1)
                case "villains":
                    dict_of_buttons[item].background_color = (1,0,0,1)
                case "henchmen":
                    dict_of_buttons[item].background_color = (235/255.0, 156/255.0, 38/255.0,1)
                case "heroes":
                    dict_of_buttons[item].background_color = (48/255.0,99/255.0,194/255.0,1)

            dict_of_buttons[item].bind(on_release = lambda instance : instance.remove_element_from_game(instance,category))

            def delete_yourself(instance):
                container = instance.parent
                container.remove_widget(instance)
                container.height = container.height - 55
                if len(container.children) <= 1:
                    container.parent.remove_widget(container)

            delete_yourself_button = lambda instance : delete_yourself(instance)
            
            dict_of_buttons[item].bind(on_release = delete_yourself_button)



            box.height = box.height + 55                                      
            box.add_widget(dict_of_buttons[item])

        
            #dict_of_buttons[item] = List_Item_Button()
            #dict_of_buttons[item].text = {}.format(item)
            #self.add_widget(dict_of_buttons[item])

            
