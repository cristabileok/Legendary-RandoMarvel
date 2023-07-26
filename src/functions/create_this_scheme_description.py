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

def create_this_scheme_description(btn,scheme):
        
    if scheme == "":
        pass
    else:
        app = App.get_running_app()
                    
        app.root.get_screen("scheme_window").ids.scheme_container.clear_widgets()

        app.root.get_screen("scheme_window").ids.scheme_title.text="{}".format(scheme.replace("|",""))
        app.root.get_screen("scheme_window").ids.scheme_title.background_color=(45/255.0, 145/255.0, 73/255.0, 1)

        ItemsAccordion = Accordion(orientation = "vertical")
        app.root.get_screen("scheme_window").ids.scheme_container.add_widget(ItemsAccordion)

        try:
            content = schemes_dict_desc[scheme].split("\n---\n")

        except KeyError:
            
            scheme = "".join(["|", scheme])
            content = schemes_dict_desc[scheme].split("\n---\n")

        for item in content:
            title,description = item.split("\n--\n")
            
            accordionitem = AccordionItem(title="{}".format(title))
            ItemsAccordion.add_widget(accordionitem)

            scroll = ScrollView()
            accordionitem.add_widget(scroll)
            if item == content[0]:
                accordionitem.collapse=False
            
            label = Label_Scroll()
            label.text = "{}".format(description)
            scroll.add_widget(label)

        keywords = schemes_dict_keys[scheme]

        if len(keywords) != []:
            for kw in keywords:
                if "Scheme Transforms" in kw:
                    _ , SchTranTarget = kw.split(":")
                    button = Button(size_hint_y = .15)
                    button.text="{}".format(kw.replace("|","").replace(":",":\n"))
                    button.background_color= (45/255, 145/255, 73/255, 1)
                    schemetransform = lambda : create_this_scheme_description(button,SchTranTarget)
                    button.on_release = schemetransform
                    app.root.get_screen("scheme_window").ids.scheme_container.add_widget(button)

                elif "Veiled Scheme" in kw:
                    unveiled_schemes = [item for item in schemes_names if "|..." in item]

                    #[ expression for item in iterable if condition ]

                    randomizer = random.randint(0,len(unveiled_schemes)-1)
                    chosen_scheme = unveiled_schemes[randomizer]

                    button = Button(size_hint_y = .15)
                    button.text="Unveil Scheme"
                    button.background_color= (45/255, 145/255, 73/255, 1)
                    

                    def unveil_scheme(button,chosen_scheme):
                        app = App.get_running_app()                    
                        app.root.get_screen("main_window").ids.scheme_lab.text = "{}".format(chosen_scheme.replace("|",""))

                        create_this_scheme_description(button,chosen_scheme)
                     
                    unveil_scheme_button = lambda : unveil_scheme(button,chosen_scheme)

                    button.on_release = unveil_scheme_button

                                        
                    app.root.get_screen("scheme_window").ids.scheme_container.add_widget(button)


                else:

                    item = AccordionItem(title=("Keyword: {}".format(kw)))
                    item.background_normal="atlas://data/images/defaulttheme/button_disabled"
                    item.background_selected="atlas://data/images/defaulttheme/button_disabled_pressed"
                    ItemsAccordion.add_widget(item)

                    scroll = ScrollView()
                    item.add_widget(scroll)

                    label = Label_Scroll()
                    label.text = "{}".format(keywords_dict[kw])
                    
                                    
                    scroll.add_widget(label)


        app = App.get_running_app()
        #app.root.get_screen("main_window").manager.transition.direction = "left"
        #app.root.get_screen("main_window").manager.current = "scheme_window"
        target_screen = app.root.get_screen("scheme_window")
        app.root.get_screen("main_window").manager.transition.direction = "left"
        app.onNextScreen(btn,target_screen)
        #app.root.get_screen("main_window").ids.scheme_lab.text = "{}".format(scheme.replace("|",""))