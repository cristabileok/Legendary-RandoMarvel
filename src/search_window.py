from kivy.uix.screenmanager import Screen

from .main_window import Main_Window

from .functions.search_input import search_input


class Search_Window(Screen):

    def search_button(self):
        search_input(self)