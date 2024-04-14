from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from ..label_scroll import Label_Scroll

from ..database import (
    masterminds_names,
    schemes_names,
    villains_names,
    henchmen_names,
    heroes_names,
    keywords_dict,
    masterminds_to_keywords,
    villains_dict,
    henchmen_dict,
    heroes_dict,
    schemes_dict_desc,
    schemes_dict_keys,
    keywords_names
)

def create_keywords_list(carrier,dict,title):
                        
        if carrier == "":
            pass
        else:
            app = App.get_running_app()
                        
            app.root.get_screen("keywords_window").ids.accordion_container.clear_widgets()

            carriers_text_clean = carrier.replace("Epic ","").replace(" \n(2 cards in deck, 2 cards in city)","")

            if title == "Mastermind" or title in masterminds_names:
                app.root.get_screen("keywords_window").ids.keywords_title.text = "{}'s Keywords".format(title)
                app.root.get_screen("keywords_window").ids.keywords_title.background_color=(119/255.0, 50/255.0, 168/255.0,1)
                
            elif title == "Villains" or title in villains_names:
                app.root.get_screen("keywords_window").ids.keywords_title.text = "{}' Keywords".format(title)
                app.root.get_screen("keywords_window").ids.keywords_title.background_color=(1,0,0,1)
                
            elif title == "Henchmen" or title in henchmen_names:
                app.root.get_screen("keywords_window").ids.keywords_title.text = "{}'s Keywords".format(title)
                app.root.get_screen("keywords_window").ids.keywords_title.background_color=(235/255.0, 156/255.0, 38/255.0,1)
                
            else:
                app.root.get_screen("keywords_window").ids.keywords_title.text = "{}' Keywords".format(title)
                app.root.get_screen("keywords_window").ids.keywords_title.background_color=(48/255.0,99/255.0,194/255.0,1)
                

            carriers_split = carriers_text_clean.split(" / ")
            
            all_keywords = []
            for item in carriers_split:
                all_keywords.append(dict[item])
            keywords_list = [item for sublist in all_keywords for item in sublist]
            keywords_sorted_set = sorted(set(keywords_list))

            if len(keywords_sorted_set) == 0:
                if title == "Villains" or title == "Henchmen" or title == "Heroes":
                    label_if_empty = Label(text="These {} have no Keywords".format(title), valign = 'center', halign = 'center')
                else:
                    label_if_empty = Label(text="{} has no Keywords".format(carriers_text_clean), valign = 'center', halign = 'center')
                app.root.get_screen("keywords_window").ids.accordion_container.add_widget(label_if_empty)

            else:

                keys_accordion = Accordion(orientation = "vertical")
                app.root.get_screen("keywords_window").ids.accordion_container.add_widget(keys_accordion)
                                        
                for kw in keywords_sorted_set:
                    
                    acordion_item = AccordionItem(title="{}".format(kw))
                    keys_accordion.add_widget(acordion_item)

                    if kw == keywords_sorted_set[0]:
                        acordion_item.collapse=False
                    
                    scroll = ScrollView()
                    acordion_item.add_widget(scroll)
                    
                    label = Label_Scroll()
                    label.text = "{}".format(keywords_dict[kw])
                    scroll.add_widget(label)