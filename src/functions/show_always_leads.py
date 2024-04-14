import os

from kivy.app import App

from ..database import (
    masterminds_names,
    villains_names,
    henchmen_names,
    masterminds_to_villains,
    masterminds_to_henchmen
)


def show_always_leads():
    main_window = App.get_running_app().root.get_screen("main_window")
    mastermind_text = main_window.ids.mastermind_lab.text
    villains_text = main_window.ids.villains_lab.text
    henchmen_text = main_window.ids.henchmen_lab.text
    
    if mastermind_text == "":
        pass

    else:
        mastermind_list = mastermind_text.split(" / ")
        for epic_name in mastermind_list:
            clean_name = epic_name.strip("Epic ")
            mastermind_list.remove(epic_name)
            mastermind_list.append(clean_name)

        for mastermind in mastermind_list:
            if mastermind in masterminds_names:
                if masterminds_to_villains[mastermind]:
                    villains_set = set(villains_text.split(" / "))
                    villains_set.pop()
                    villains_set.update(masterminds_to_villains[mastermind])
                    villains_list = sorted(villains_set)
                    villains_text = " / ".join(villains_list)
                    main_window.ids.villains_lab.text = "{}".format(villains_text)

                if masterminds_to_henchmen[mastermind]:
                    henchmen_set = set(henchmen_text.split(" /"))
                    henchmen_set.pop()
                    henchmen_set.update(masterminds_to_henchmen[mastermind])
                    henchmen_list = sorted(henchmen_set)
                    henchmen_text = " / ".join(henchmen_list)
                    main_window.ids.henchmen_lab.text = "{}".format(henchmen_text)     