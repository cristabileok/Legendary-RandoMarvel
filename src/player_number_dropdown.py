from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

from .functions.randomize_n_player import randomize_1_player, randomize_2_player, randomize_3_player, randomize_4_player

from .setup_numbers import SetupNumbers


class PlayerNumberDropDown(DropDown):
    def __init__(self, game_setup, **kwargs):
        super(PlayerNumberDropDown,self).__init__(**kwargs)
        self.game_setup = game_setup

    def randomize_1_player(self):
        randomize_1_player(self.game_setup)

    def randomize_2_player(self):
        randomize_2_player(self.game_setup)

    def randomize_3_player(self):
        randomize_3_player(self.game_setup)

    def randomize_4_player(self):
        randomize_4_player(self.game_setup)

    def clear_dropdown(self):
                self.dismiss()               
