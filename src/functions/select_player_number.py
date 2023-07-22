from kivy.app import App

from ..player_number_dropdown import PlayerNumberDropDown


def select_player_number(game_setup):
        player_number_dropdown = PlayerNumberDropDown(game_setup)
        player_number_dropdown.game_setup = game_setup
        main_window = App.get_running_app().root.get_screen("main_window")
        player_number_dropdown.open(main_window.ids.select_number_players_button)