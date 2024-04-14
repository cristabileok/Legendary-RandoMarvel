from kivy.app import App

from .adjust_poketset_to_input import adjust_poketset_to_henchman, adjust_poketset_to_mastermind, adjust_poketset_to_villain

def reduce(category):
    main_window = App.get_running_app().root.get_screen("main_window")
    poketset_window = App.get_running_app().root.get_screen("poketset_window")       

    match category:
        case "scheme":
            source = main_window.ids.scheme_lab
        case "masterminds":
            source = main_window.ids.mastermind_lab
        case "villains":
            source = main_window.ids.villains_lab
        case "henchmen":
            source = main_window.ids.henchmen_lab
        case "heroes":
            source = main_window.ids.heroes_lab

        case "masterminds_poketset":
            source = poketset_window.ids.poketset_masterminds
        case "villains_poketset":
            source = poketset_window.ids.poketset_villains
        case "henchmen_poketset":
            source = poketset_window.ids.poketset_henchmen
        case "heroes_poketset":
            source = poketset_window.ids.poketset_heroes

    list = source.text.split(" / ")
    element_to_remove = list.pop()
    new_text = " / ".join(list)
    source.text = f"{new_text}"
    
    if category == "masterminds_poketset":
        adjust_poketset_to_mastermind(element_to_remove)
    elif category == "villains_poketset":
        adjust_poketset_to_villain(element_to_remove)
    elif category == "henchmen_poketset":
        adjust_poketset_to_henchman(element_to_remove)