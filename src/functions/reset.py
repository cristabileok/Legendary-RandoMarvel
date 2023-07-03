from kivy.app import App

def reset(game_setup):
    game_setup.number_of_villains = 1
    game_setup.number_of_henchmen = 1
    game_setup.number_of_heroes = 1

    main_window = App.get_running_app().root.get_screen("main_window")
    main_window.ids.instructions.text="Select Number of Players\nor Categories to be Randomized"
    main_window.ids.scheme_lab.text=''
    main_window.ids.mastermind_lab.text=''
    main_window.ids.villains_lab.text=''
    main_window.ids.henchmen_lab.text=''
    main_window.ids.heroes_lab.text=''
    main_window.ids.bystanders_lab.text=''