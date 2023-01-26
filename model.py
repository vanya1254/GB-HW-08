dict_class = dict()
dict_lesson = dict()
choice_class = ''
choice_lesson = ''
choice_pupil = ()
list_lessons = ['Русский', 'Английский', 'Математика']
list_classes = ['7А', '7Б', '7В']


def get_dict_class():
    global dict_class
    return dict_class


def get_list_lessons():
    global list_lessons
    return list_lessons


def get_list_classes():
    global list_classes
    return list_classes


def get_dict_lesson():
    global dict_lesson
    return dict_lesson


def get_choice_pupil():
    global choice_pupil
    return choice_pupil


def clear_class_data():
    global dict_class
    global dict_lesson
    global choice_pupil
    dict_class = dict()
    dict_lesson = dict()
    choice_pupil = ()


def clear_lesson_data():
    global dict_lesson
    global choice_pupil
    dict_lesson = dict()
    choice_pupil = ()


def clear_pupil_data():
    global choice_pupil
    choice_pupil = ()


def read_class(string: str):
    global dict_class
    global choice_class
    choice_class = string.upper()
    path = 'classes/' + string.upper() + ".txt"
    temp = ''
    list_pupil = []
    
    with open(path, 'r', encoding='UTF-8') as file:
        temp = file.readlines()
        
        for i in range(len(temp)):
            temp[i] = temp[i].strip().split(' - ')
            temp[i][1] = temp[i][1].split('; ')
            dict_lesson = dict()
            
            for j in range(len(temp[i][1])):
                list_pupil = temp[i][1][j].split(': ')
                dict_lesson.setdefault(f'{list_pupil[0]}', list_pupil[1].strip('[]').rstrip(';').rstrip(']').split(', '))
                dict_class.setdefault(f'{temp[i][0]}', dict_lesson)
    
        return dict_class


def read_lesson(string: str):
    global dict_class
    global dict_lesson
    global choice_lesson

    for k in dict_class.keys():
        if k == string:
            dict_lesson = dict_class[k]
            choice_lesson = k
        else:
            pass


def get_pupil(pupil):
    global dict_lesson
    global choice_pupil
    
    for k, v in dict_lesson.items():
        if k.lower() == pupil.lower():
            choice_pupil = k, v
            return choice_pupil
        else:
            pass


def check_open_class():
    global dict_class
    return bool(dict_class)


def check_open_lesson():
    global dict_lesson
    return bool(dict_lesson)


def check_get_pupil():
    global choice_pupil
    return bool(choice_pupil)


def set_mark_pupil(mark):
    global choice_pupil
    name, marks = choice_pupil
    marks.append(mark)
    choice_pupil = name, marks


def save_mark_pupil():
    global dict_class
    global dict_lesson
    global choice_pupil
    global choice_lesson
    key, value = choice_pupil
    
    dict_lesson[key] = value
    dict_class[choice_lesson] = dict_lesson
    choice_lesson = ''
    choice_pupil = ()


def write_class():
    global dict_class
    global choice_class
    path = 'classes/' + choice_class + ".txt"
    
    with open(path, 'w', encoding='UTF-8') as file:
        for key, val in dict_class.items():
            file.writelines(f'{key} -')
            for k, v in val.items():
                file.writelines(f' {k}: {list(map(int, v))};')
            file.writelines(f'\n')


def exit_program():
    exit()