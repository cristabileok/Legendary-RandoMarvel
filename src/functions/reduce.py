from kivy.app import App

def reduce_scheme():
    main_window = App.get_running_app().root.get_screen("main_window")
    old_text = main_window.ids.scheme_lab.text
    list = old_text.split(" / ")
    _ = list.pop()
    new_text = " / ".join(list)
    main_window.ids.scheme_lab.text = "{}".format(new_text)
    
def reduce_mastermind():
    main_window = App.get_running_app().root.get_screen("main_window")
    old_text = main_window.ids.mastermind_lab.text
    list = old_text.split(" / ")
    _ = list.pop()
    new_text = " / ".join(list)
    main_window.ids.mastermind_lab.text = "{}".format(new_text)
    
def reduce_villains():
    main_window = App.get_running_app().root.get_screen("main_window")
    old_text = main_window.ids.villains_lab.text
    list = old_text.split(" / ")
    _ = list.pop()
    new_text = " / ".join(list)
    main_window.ids.villains_lab.text = "{}".format(new_text)
    
def reduce_henchmen():
    main_window = App.get_running_app().root.get_screen("main_window")
    old_text = main_window.ids.henchmen_lab.text
    list = old_text.split(" / ")
    _ = list.pop()
    new_text = " / ".join(list)
    main_window.ids.henchmen_lab.text = "{}".format(new_text)
    
def reduce_heroes():
    main_window = App.get_running_app().root.get_screen("main_window")
    old_text = main_window.ids.heroes_lab.text
    list = old_text.split(" / ")
    _ = list.pop()
    new_text = " / ".join(list)
    main_window.ids.heroes_lab.text = "{}".format(new_text)