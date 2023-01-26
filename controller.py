from model import *
from view import *


def input_handler(inp: int):
    match inp:
        case 1:
            clear_class_data()
            read_class(input_class(get_list_classes()))
        case 2:
            if check_open_class():
                clear_lesson_data()
                read_lesson(input_lesson(get_list_lessons()))
            else:
                show_status_class(check_open_class())
        case 3:
            if check_open_class() and check_open_lesson():
                clear_pupil_data()
                show_pupil(get_pupil(input_pupil()))
            else:
                show_status_class(check_open_class())
                show_status_lesson(check_open_lesson())
        case 4:
            if check_get_pupil():
                set_mark_pupil(input_mark())
                show_pupil(get_choice_pupil())
                save_mark_pupil()
            else:
                show_status_pupil(check_get_pupil())
        case 5:
            if check_open_lesson():
                show_lesson(get_dict_lesson())
            else:
                show_status_lesson(check_open_lesson())
        case 6:
            if check_open_class():
                show_all(get_dict_class())
            else:
                show_status_class(check_open_class())
        case 7:
            if check_open_class():
                write_class()
                clear_class_data()
            else:
                show_status_class(check_open_class())
        case 8:
            show_exit()
            exit_program()


def start():
    while True:
        user_choice = main_menu()
        input_handler(user_choice)