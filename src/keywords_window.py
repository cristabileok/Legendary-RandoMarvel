from kivy.uix.screenmanager import Screen

from .main_window import Main_Window

class Keywords_Window(Screen):
    def Go_Search(self):
        proxy = Main_Window()
        proxy.Go_To_Search()