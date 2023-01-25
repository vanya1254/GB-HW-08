from model import *
from view import *


def input_handler(inp: int):
    match inp:
        case 1:
            read_class(input_class(get_list_classes()))
        case 2:
            show_lesson(read_lesson(input_lesson(get_list_lessons())))
        case 3:
            show_all(get_dict_class())
        case 4:
            get_pupil(find_pupil(show_lesson()))
        case 7:
            exit_program()
            

def start():
    while True:
        user_choice = main_menu()
        input_handler(user_choice)