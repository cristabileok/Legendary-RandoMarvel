from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App

from .functions.adjust_poketset_to_input import adjust_poketset_to_mastermind,adjust_poketset_to_villain,adjust_poketset_to_henchman


class List_Item_Button(Button):
    
    def remove_item(self, instance):
        self.parent.remove_widget(self)

    def remove_parent_dropdown(self, instance):
        #self.parent.parent.parent.parent.remove_widget(self.parent.parent.parent)
        self.parent.parent.parent.dismiss()
        
    def set_to_game(self, instance):
        
        app = App.get_running_app()
        
        text = self.parent.children[1].text
    
        app.root.get_screen("main_window").ids.scheme_lab.text = "{}".format(text)

    def get_source(self,category):
        app = App.get_running_app()
        match category:
            case "masterminds":
                source = app.root.get_screen("main_window").ids.mastermind_lab
            case "villains":
                source = app.root.get_screen("main_window").ids.villains_lab
            case "henchmen":
                source = app.root.get_screen("main_window").ids.henchmen_lab
            case "heroes":
                source = app.root.get_screen("main_window").ids.heroes_lab

            case "masterminds_poketset":
                source = app.root.get_screen("poketset_window").ids.poketset_masterminds
            case "villains_poketset":
                source = app.root.get_screen("poketset_window").ids.poketset_villains
            case "henchmen_poketset":
                source = app.root.get_screen("poketset_window").ids.poketset_henchmen
            case "heroes_poketset":
                source = app.root.get_screen("poketset_window").ids.poketset_heroes


        return source

    def add_element_to_game(self,instance,trigger,category):
        new_text = trigger.parent.children[1].text

        source = self.get_source(category)

        old_text = source.text
                      
        if old_text == "":
            new_game_list = new_text
            
        elif new_text in old_text or old_text in new_text:
            new_game_list = old_text
            
        else:        
            new_game_list = old_text + " / " + new_text

        source.text = f"{new_game_list}"

    def add_element_to_poketset(self,instance,trigger,category):
        new_text = trigger.parent.children[1].text

        match category:
            case "masterminds":
                category = "masterminds_poketset"
            case "villains":
                category = "villains_poketset"
            case "henchmen":
                category = "henchmen_poketset"
            case "heroes":
                category = "heroes_poketset"

        source = self.get_source(category)

        old_text = source.text

        if old_text == "":
            new_poketset_list = new_text

        elif new_text in old_text or old_text in new_text:
            new_poketset_list = old_text

        else:
            new_poketset_list = old_text + " / " + new_text

        source.text = f"{new_poketset_list}"

        if category == "masterminds_poketset":
             adjust_poketset_to_mastermind(new_text)
        elif category == "villains_poketset":
            adjust_poketset_to_villain(new_text)
        elif category == "henchmen_poketset":
            adjust_poketset_to_henchman(new_text)
            

    def remove_element_from_game(self,instance,category):
        app = App.get_running_app()

        element_to_remove = self.text

        source = self.get_source(category)

        old_text = source.text
           
        if old_text == "":
            pass
            
        elif element_to_remove in old_text or old_text in element_to_remove:
            old_list = old_text.split(" / ")
            old_list.remove(element_to_remove)
            new_game_list = " / ".join(old_list)

        source.text = f"{new_game_list}"

        if category == "masterminds_poketset":
             adjust_poketset_to_mastermind(element_to_remove)
        elif category == "villains_poketset":
            adjust_poketset_to_villain(element_to_remove)
        elif category == "henchmen_poketset":
            adjust_poketset_to_henchman(element_to_remove)

        

