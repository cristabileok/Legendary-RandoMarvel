
from kivy.app import App

from kivy.lang import Builder

from src.keywords_window import Keywords_Window
from src.main_window import Main_Window
from src.scheme_window import Scheme_Window
from src.search_window import Search_Window
from src.window_manager import WindowManager

ux = Builder.load_file("gui/gui.kv")    

class RandoMarvel(App):
    def build(self):

        #root_folder = self.user_data_dir
        
        return ux

            

if __name__ == "__main__":
    RandoMarvel().run()