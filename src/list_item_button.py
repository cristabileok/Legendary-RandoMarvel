from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App


class List_Item_Button(Button):
    
    def remove_item(self, instance):
        self.parent.remove_widget(self)
        
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
        return source

    def add_element_to_game(self,instance,category):
        
        new_text = self.parent.children[1].text

        source = self.get_source(category)

        old_text = source.text
                      
        if old_text == "":
            new_game_list = new_text
            
        elif new_text in old_text or old_text in new_text:
            new_game_list = old_text
            
        else:        
            new_game_list = old_text + " / " + new_text

        source.text = f"{new_game_list}"
            

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

