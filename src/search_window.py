from kivy.uix.screenmanager import Screen

from .main_window import Main_Window

class Search_Window(Screen):
    def search_button(self):
        proxy = Main_Window()
        proxy.search_input()