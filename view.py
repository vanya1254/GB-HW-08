def main_menu():
    print('\nВыберите команду:')     
    menu_list = ['Выбрать класс',
                 'Выбрать предмет',
                 'Показать всех учеников класса',
                 'Кто пойдет к доске?',
                 'На какую оценку ответил ученик?',
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
    print(f'\nСписок учеников класса по предмету:')
    for k, v in dict_.items():
        print(f'\t{k}: {list(map(int, v))}')


def show_all(dict_):
    print(f'\nСписок всех учеников класса:')
    for key, val in dict_.items():
        print(f'\n\t{key}:\n')
        for k, v in val.items():
            print(f'\t\t{k}: {list(map(int, v))}')


def find_pupil(choice):
    user_pupil = input(f'\nВведите фамилию и имя ученика ("Иванов Иван") => ')
    return user_pupil, choice


