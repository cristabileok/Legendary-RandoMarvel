from kivy.uix.screenmanager import Screen

from .main_window import Main_Window
from .functions.go_to_search import go_to_search

class Scheme_Window(Screen):
    def go_to_search(self,btn):
        go_to_search(btn)