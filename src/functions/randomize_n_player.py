from .show_elements import *

def randomize_1_player(game_setup):
    game_setup.set_player_1()
    show_randomized_schemes(1)
    show_randomized_mastermind(1)
    show_randomized_villains(game_setup.number_of_villains)
    show_randomized_henchmen(game_setup.number_of_henchmen,game_setup.number_of_heroes)
    show_randomized_heroes(game_setup.number_of_heroes)
    show_bystanders(1)

def randomize_2_player(game_setup):
    game_setup.set_player_2()
    show_randomized_schemes(1)
    show_randomized_mastermind(1)
    show_randomized_villains(game_setup.number_of_villains)
    show_randomized_henchmen(game_setup.number_of_henchmen,game_setup.number_of_heroes)
    show_randomized_heroes(game_setup.number_of_heroes)
    show_bystanders(2)

def randomize_3_player(game_setup):
    game_setup.set_player_3()
    show_randomized_schemes(1)
    show_randomized_mastermind(1)
    show_randomized_villains(game_setup.number_of_villains)
    show_randomized_henchmen(game_setup.number_of_henchmen,game_setup.number_of_heroes)
    show_randomized_heroes(game_setup.number_of_heroes)
    show_bystanders(8)

def randomize_4_player(game_setup):
    game_setup.set_player_4()
    show_randomized_schemes(1)
    show_randomized_mastermind(1)
    show_randomized_villains(game_setup.number_of_villains)
    show_randomized_henchmen(game_setup.number_of_henchmen,game_setup.number_of_heroes)
    show_randomized_heroes(game_setup.number_of_heroes)
    show_bystanders(8)