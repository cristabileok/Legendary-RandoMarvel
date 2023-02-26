
from kivy.app import App

from kivy.lang import Builder

from src.keywords_window import Keywords_Window
from src.main_window import Main_Window
from src.scheme_window import Scheme_Window
from src.search_window import Search_Window
from src.window_manager import WindowManager


class RandoMarvel(App):
    
    def on_start(self):
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            app = App.get_running_app()
            if app.root.get_screen("main_window") != "main_window":
                app.root.get_screen("main_window").manager.transition.direction = "right"
                app.root.get_screen("main_window").manager.current = "main_window"
        # do what you want, return True for stopping the propagation
            return True
        
    
    def build(self):
        
        ux = Builder.load_file("gui/gui.kv")    

        #root_folder = self.user_data_dir
        
        return ux

            

if __name__ == "__main__":
    RandoMarvel().run()