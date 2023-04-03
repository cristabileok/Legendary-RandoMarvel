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
                               

    def add_mastermind_to_game(self,instance):
        
        app = App.get_running_app()
                
        new_text = self.parent.children[1].text
        
        old_text = app.root.get_screen("main_window").ids.mastermind_lab.text
        
        if old_text == "":
            new_game_list = new_text
            
        else:        
            new_game_list = old_text + " / " + new_text
        
        app.root.get_screen("main_window").ids.mastermind_lab.text = "{}".format(new_game_list)
        
    def add_villains_to_game(self,instance):
        
        app = App.get_running_app()
                
        new_text = self.parent.children[1].text
        
        old_text = app.root.get_screen("main_window").ids.villains_lab.text
        
        if old_text == "":
            new_game_list = new_text
            
        else:        
            new_game_list = old_text + " / " + new_text
        
        app.root.get_screen("main_window").ids.villains_lab.text = "{}".format(new_game_list)
        
    def add_henchmen_to_game(self,instance):
        
        app = App.get_running_app()
                
        new_text = self.parent.children[1].text
        
        old_text = app.root.get_screen("main_window").ids.henchmen_lab.text
        
        if old_text == "":
            new_game_list = new_text
            
        else:        
            new_game_list = old_text + " / " + new_text
        
        app.root.get_screen("main_window").ids.henchmen_lab.text = "{}".format(new_game_list)
        
    def add_heroes_to_game(self,instance):
        
        app = App.get_running_app()
                
        new_text = self.parent.children[1].text
        
        old_text = app.root.get_screen("main_window").ids.heroes_lab.text
        
        if old_text == "":
            new_game_list = new_text
            
        else:        
            new_game_list = old_text + " / " + new_text
        
        app.root.get_screen("main_window").ids.heroes_lab.text = "{}".format(new_game_list)