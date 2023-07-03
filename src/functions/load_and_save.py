import os

from kivy.app import App


def save_game(number_of_villains,number_of_henchmen,number_of_heroes):
    main_window = App.get_running_app().root.get_screen("main_window")
    scheme_save = main_window.ids.scheme_lab.text
    mastermind_save = main_window.ids.mastermind_lab.text
    villains_save = main_window.ids.villains_lab.text
    henchmen_save = main_window.ids.henchmen_lab.text
    heroes_save = main_window.ids.heroes_lab.text
    bystanders_save = main_window.ids.bystanders_lab.text
    lines = [str(number_of_villains),str(number_of_henchmen),str(number_of_heroes),scheme_save,mastermind_save,villains_save,henchmen_save,heroes_save,bystanders_save]
    with open(os.path.join(os.path.dirname(__file__),'../../lists/saved_game.txt'), 'w') as save:
        save.write('\n'.join(lines))

def load_game():
    main_window = App.get_running_app().root.get_screen("main_window")
    game_to_load = open(os.path.join(os.path.dirname(__file__),'../../lists/saved_game.txt'), 'r')
    if len(game_to_load.read().splitlines()) != 9:
        pass
    else:
        game_to_load = open(os.path.join(os.path.dirname(__file__),'../../lists/saved_game.txt'), 'r')
        number_of_villains,number_of_henchmen,number_of_heroes,scheme_load,mastermind_load,villains_load,henchmen_load,heroes_load,bystanders_load = game_to_load.read().splitlines()
        number_of_villains = int(number_of_villains)
        number_of_henchmen = int(number_of_henchmen)
        number_of_heroes = int(number_of_heroes)
        main_window.ids.scheme_lab.text = '{}'.format(scheme_load)
        main_window.ids.mastermind_lab.text = '{}'.format(mastermind_load)
        main_window.ids.villains_lab.text = '{}'.format(villains_load)
        main_window.ids.henchmen_lab.text = '{}'.format(henchmen_load)
        main_window.ids.heroes_lab.text = '{}'.format(heroes_load)
        main_window.ids.bystanders_lab.text = '{}'.format(bystanders_load)
        return number_of_villains, number_of_henchmen, number_of_heroes