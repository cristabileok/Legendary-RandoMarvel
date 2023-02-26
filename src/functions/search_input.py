from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button

import random

from ..label_scroll import Label_Scroll

from ..database import (
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

def search_input(self):
    
        app = App.get_running_app()
        input = (app.root.get_screen("search_window").ids.textinput.text).lower()
        
        app.root.get_screen("search_window").ids.search_container.clear_widgets()

        if len(input) <= 3:
            
            label = Label()
            label.text = "Input at least 4 letters to search"
            app.root.get_screen("search_window").ids.search_container.clear_widgets()
            app.root.get_screen("search_window").ids.search_container.add_widget(label)

        else:

            button = {}
            button_list = []
            content_list = {}
            show_desc = {}
            show_keys = {}
            findings_counter = 0
            
            for name in schemes_names:
                if (input in name.lower()) or (input in str(schemes_dict_desc[name]).lower()) or (input in str(schemes_dict_keys[name]).lower()):
                    
                    button[name] = Button()
                    app.root.get_screen("search_window").ids.search_container.add_widget(button[name])
                    button_list.append(button[name])
                    content_list[button[name]] = name
                    
                    button[name].text="{}".format(name.replace("|",""))
                    button[name].background_color= (45/255, 145/255, 73/255, 1)
                    findings_counter += 1


            for item in button_list:
                show_desc[item] = lambda item : self.create_this_scheme_description(content_list[item])
                item.bind(on_release = show_desc[item])

            button_list = []

            for name in masterminds_names:
                if (input in name.lower()) or (input in str(masterminds_dict[name]).lower()):
                    
                    button[name] = Button()
                    app.root.get_screen("search_window").ids.search_container.add_widget(button[name])
                    button_list.append(button[name])
                    content_list[button[name]] = name
                    
                    button[name].text="{}".format(name)
                    button[name].background_color= (119/255.0, 50/255.0, 168/255.0,1)
                    
                    findings_counter += 1
                    
            for item in button_list:
                show_keys[item] = lambda item : self.show_keywords_list(content_list[item],masterminds_dict,content_list[item])
                item.bind(on_release = show_keys[item])

            button_list = []        

            for name in villains_names:
                if (input in name.lower()) or (input in str(villains_dict[name]).lower()):
                    
                    button[name] = Button()
                    app.root.get_screen("search_window").ids.search_container.add_widget(button[name])
                    button_list.append(button[name])
                    content_list[button[name]] = name
                    
                    button[name].text="{}".format(name)
                    button[name].background_color= (1,0,0,1)
                    
                    findings_counter += 1
                    
            for item in button_list:
                show_keys[item] = lambda item : self.show_keywords_list(content_list[item],villains_dict,content_list[item])
                item.bind(on_release = show_keys[item])

            button_list = []    


            for name in henchmen_names:
                if (input in name.lower()) or (input in str(henchmen_dict[name]).lower()):
                    
                    button[name] = Button()
                    app.root.get_screen("search_window").ids.search_container.add_widget(button[name])
                    button_list.append(button[name])
                    content_list[button[name]] = name
                    
                    button[name].text="{}".format(name)
                    button[name].background_color= (235/255.0, 156/255.0, 38/255.0,1)
                    
                    findings_counter += 1
                    
            for item in button_list:
                show_keys[item] = lambda item : self.show_keywords_list(content_list[item],henchmen_dict,content_list[item])
                item.bind(on_release = show_keys[item])

            button_list = []
            for name in heroes_names:
                
                if (input in name.lower()) or (input in str(heroes_dict[name]).lower()):
                                                    
                    button[name] = Button()
                    app.root.get_screen("search_window").ids.search_container.add_widget(button[name])
                    button_list.append(button[name])
                    content_list[button[name]] = name
                    
                    button[name].text="{}".format(name)
                    button[name].background_color= (48/255.0,99/255.0,194/255.0,1)
                    
                    findings_counter += 1
                                                                
            for item in button_list:
                show_keys[item] = lambda item : self.show_keywords_list(content_list[item],heroes_dict,content_list[item])
                item.bind(on_release = show_keys[item])

            button_list = []
            
            if findings_counter == 0:
                label = Label()
                label.text = "No matches found on this search.\nTry a different input."
                app.root.get_screen("search_window").ids.search_container.clear_widgets()
                app.root.get_screen("search_window").ids.search_container.add_widget(label)
            

            def KeywordDescriptThis(Keyword):
                app = App.get_running_app()
                app.root.get_screen("scheme_window").ids.scheme_container.clear_widgets()

                app.root.get_screen("scheme_window").ids.scheme_title.text="{}".format(Keyword)
                app.root.get_screen("scheme_window").ids.scheme_title.background_color=(0,0,8/10.0,1)

                scroll = ScrollView()
                app.root.get_screen("scheme_window").ids.scheme_container.add_widget(scroll)

                label = Label_Scroll()
                label.text = "{}".format(keywords_dict[Keyword])
                scroll.add_widget(label)

                app = App.get_running_app()
                app.root.get_screen("main_window").manager.transition.direction = "left"
                app.root.get_screen("main_window").manager.current = "scheme_window" 


            for name in keywords_names:
                if "Scheme Transforms" in name:
                    pass
                elif (input in name) or (input.capitalize() in name) or (input.upper() in name) or (input.lower() in name) or (input.title() in name):
                    
                    button[name] = Button()
                    app.root.get_screen("search_window").ids.search_container.add_widget(button[name])
                    button_list.append(button[name])
                    content_list[button[name]] = name
                    
                    button[name].text="{}".format(name)
                    button[name].background_color= (0,0,8/10.0,1)
                    
            for item in button_list:
                show_keys[item] = lambda item : KeywordDescriptThis(content_list[item])
                item.bind(on_release = show_keys[item])

            button_list = []        