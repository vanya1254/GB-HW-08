dict_class = dict()
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


def set_db(data: str):
    global dict_class
    dict_class.append(data)


def read_class(string: str):
    global dict_class
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


def read_lesson(string: str):
    global dict_class
    
    for k in dict_class.keys():
        if k == string:
            return dict_class[k]
        else:
            pass


def get_pupil(pupil, choice):
    global dict_class
    
    for key in dict_class.keys():
        if key == choice:
            for k, v in dict_class[key].items():
                