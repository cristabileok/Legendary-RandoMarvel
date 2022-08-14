from kivy.uix.screenmanager import Screen

from .main_window import Main_Window

class Search_Window(Screen):
    def Search_Button(self):
        proxy = Main_Window()
        proxy.Search_input()