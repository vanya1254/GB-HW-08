dict_class = dict()

def read_class(string: str):
    global dict_class
    path = 'classes/7А.txt' #+ string.upper() + ".txt"
    temp = ''
    list_puple = []
    
    with open(path, 'r', encoding='UTF-8') as file:
        temp = file.readlines()
        
        for i in range(len(temp)):
            temp[i] = temp[i].strip().split(' - ')
            temp[i][1] = temp[i][1].split('; ')
            dict_lesson = dict()
            
            for j in range(len(temp[i][1])):
                list_puple = temp[i][1][j].split(': ')
                dict_lesson.setdefault(f'{list_puple[0]}', list_puple[1].strip('[]').strip(';').split(', '))
                dict_class.setdefault(f'{temp[i][0]}', dict_lesson)


