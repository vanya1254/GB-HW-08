def main_menu():
    print('\nВыберите команду:')     
    menu_list = ['Выбрать класс',
                 'Выбрать предмет',
                 'Выбрать ученика',
                 'Поставить оценку ученику',
                 'Показать всех учеников класса по предмету',
                 'Показать всех учеников класса',
                 'Сохранить изменения',
                 'Закрыть'
                ]
    
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')
    user_choice = int(input('\nВведите номер => '))
    
    return user_choice


def input_class(list_):
    print('\nВыбрать класс:\n',
          f'\t1. {list_[0]}\n',
          f'\t2. {list_[1]}\n',
          f'\t3. {list_[2]}\n',)
    
    user_choice = int(input(f'\nВведите номер => ')) - 1
    user_choice = list_[user_choice]
    return user_choice


def input_lesson(list_):
    print('\nВыбрать предмет:\n',
          f'\t1. {list_[0]}\n',
          f'\t2. {list_[1]}\n',
          f'\t3. {list_[2]}\n',)
    
    user_choice = int(input(f'\nВведите номер => ')) - 1
    user_choice = list_[user_choice]
    return user_choice


def show_lesson(dict_):
    print(f'\nСписок учеников класса по предмету:\n')
    for k, v in dict_.items():
        print(f'\t{k}: {list(map(int, v))}')


def show_all(dict_):
    print(f'\nСписок всех учеников класса:')
    for key, val in dict_.items():
        print(f'\n\t{key}:\n')
        for k, v in val.items():
            print(f'\t\t{k}: {list(map(int, v))}')


def input_pupil():
    user_pupil = input(f'\nВведите фамилию и имя ученика ("Иванов Иван") => ')
    return user_pupil


def show_pupil(pupil):
    name, marks = pupil
    print(f'\nВаш ученик:')
    print(f'\t{name}: {list(map(int, marks))}')


def show_status_class(bool):
    if bool:
        print(f'\nКласс выбран')
    else:
        print(f'\nКласс еще не выбран')


def show_status_lesson(bool):
    if bool:
        print(f'\nПредмет выбран')
    else:
        print(f'\nПредмет еще не выбран')


def show_status_pupil(bool):
    if bool:
        print(f'\nУченик выбран')
    else:
        print(f'\nУченик еще не выбран')


def input_mark():
    user_mark = input(f'\nВведите оценку ("5") => ')
    return user_mark


def show_exit():
    print('\n\nПрограмма закрыта')