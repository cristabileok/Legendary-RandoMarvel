from .create_keywords_list import create_keywords_list
from .go_to_keywords_description import go_to_keywords_description


def show_keywords_list(btn,carrier,dict,title):
    create_keywords_list(carrier,dict,title)
    go_to_keywords_description(btn)