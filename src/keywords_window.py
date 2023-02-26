from kivy.uix.screenmanager import Screen

from .main_window import Main_Window

class Keywords_Window(Screen):
    def go_to_search(self):
        proxy = Main_Window()
        proxy.go_to_search()