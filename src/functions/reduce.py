from kivy.app import App

def reduce(category):
    main_window = App.get_running_app().root.get_screen("main_window")
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
    list = source.text.split(" / ")
    _ = list.pop()
    new_text = " / ".join(list)
    source.text = f"{new_text}"