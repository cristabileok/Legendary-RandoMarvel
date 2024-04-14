import os

from kivy.app import App


def save_poketset():
    poketset_window = App.get_running_app().root.get_screen("poketset_window")
    masterminds_save = poketset_window.ids.poketset_masterminds.text
    villains_save = poketset_window.ids.poketset_villains.text
    henchmen_save = poketset_window.ids.poketset_henchmen.text
    heroes_save = poketset_window.ids.poketset_heroes.text
    lines = [masterminds_save,villains_save,henchmen_save,heroes_save]
    with open(os.path.join(os.path.dirname(__file__),'../../lists/saved_poketset.txt'), 'w') as save:
        save.write('\n'.join(lines))

def load_poketset():
    poketset_window = App.get_running_app().root.get_screen("poketset_window")
    game_to_load = open(os.path.join(os.path.dirname(__file__),'../../lists/saved_poketset.txt'), 'r')
    if len(game_to_load.read().splitlines()) != 4:
        pass
    else:
        game_to_load = open(os.path.join(os.path.dirname(__file__),'../../lists/saved_poketset.txt'), 'r')
        masterminds_load,villains_load,henchmen_load,heroes_load = game_to_load.read().splitlines()
        poketset_window.ids.poketset_masterminds.text = '{}'.format(masterminds_load)
        poketset_window.ids.poketset_villains.text = '{}'.format(villains_load)
        poketset_window.ids.poketset_henchmen.text = '{}'.format(henchmen_load)
        poketset_window.ids.poketset_heroes.text = '{}'.format(heroes_load)