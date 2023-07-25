
from kivy.app import App

from kivy.lang import Builder

from src.keywords_window import Keywords_Window
from src.main_window import Main_Window
from src.scheme_window import Scheme_Window
from src.search_window import Search_Window
from src.window_manager import WindowManager


class RandoMarvel(App):
    def __init__(self, *args, **kwargs):
        super(RandoMarvel, self).__init__(*args, **kwargs)
        self.list_of_prev_screens = []

    def onNextScreen(self, btn, next_screen):
        # add screen we were just in
        self.list_of_prev_screens.append(self.root.get_screen("main_window").manager.current)
        # Go to next screen
        self.root.get_screen("main_window").manager.current = next_screen.name           
    
    def on_start(self):
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            return self.onBackBtn()
                
        # do what you want, return True for stopping the propagation
            #return True
        
    def onBackBtn(self):
        # Check if there are any screens to go back to
        if self.list_of_prev_screens:
            # If there are then just go back to it
            self.root.get_screen("main_window").manager.transition.direction = "right"
            self.root.get_screen("main_window").manager.current = self.list_of_prev_screens.pop()            
            print(f"Lista de pantallas (back button):{self.list_of_prev_screens}")
            # We don't want to close app
            return True
        # No more screens so user must want to exit app > But I want it open so let's keep it True
        return True
        
    
    def build(self):
        
        ux = Builder.load_file("gui/gui.kv")    

        #root_folder = self.user_data_dir
        
        return ux

            

if __name__ == "__main__":
    RandoMarvel().run()