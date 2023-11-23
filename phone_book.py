import os
# Дополнить справочник возможностью копирования данных из одного файла в другой. 
# Пользователь вводит номер строки,
# которую необходимо перенести из одного файла в другой.

def print_dir():
    """ функция для отображения директории
    """
    lst_files = [i for i in os.listdir() if os.path.isfile(i)]
    index = 1
    
    for _ in lst_files:
        print(index," ",lst_files[index-1]) # выводим  файлы на экран
        index += 1

def coppy_lines():
    print("Список файлов для поиска ")
    
    lst_files = [i for i in os.listdir() if os.path.isfile(i)]    # список который содержит файлы
    
    print_dir()              # вывод файлов файлы
        
    user_choice = input("Введите номер файла или х чтобы выйти ")
    
    if 1<= int(user_choice) <= len(lst_files):
        file = lst_files[int(user_choice) - 1]               # выбор  файла
    
    else:
        return
    
    with open(file,encoding="utf-8") as f:
        text = f.readlines()                             # содержимое файла сохраняем в виде списка
        
    for i in range(len(text)):
        print(i+1," ",text[i])
    
    copy_index = int(input("Введите номер строки которую вы хотите скопировать "))    
    
    copy_line = text[copy_index - 1]    # вбор строки 
    
    print_dir()
        
    user_choice = input("Введите номер файла или х чтобы выйти ")
    print("Введите номер файла куда нужно сохранить скопированную строку")
    
    
    
    if 1<= int(user_choice) <= len(lst_files):
        file = lst_files[int(user_choice) - 1]
        
        
    with open(file,"a",encoding="utf-8") as f:           # копирование строки     
        f.writelines(copy_line)
        
    print("успех!")
    
    

def choice_dir():
    """ функция для просмотра директорий
    """
    print("Выберите место куда сохранить файл")
    
    my_path = ""  # пременная  для сохранения путя  
    disk = ""  # пременная  для выбора диска 
    
    print("Выберите диск")
    
    index = 1
    
    for i in os.listdrives(): # Выбор диска  D или C
        print(index," ",i)
        index += 1
        
    indx = input("Введите номер диска ")
    
    disk = str(os.listdrives()[int(indx)-1])  # Выбор диска пользователем  
    
    print("Выбирете папку")
    
    my_path += disk   # Сохраням выбранный диск в наш путь

    lst = None  # пременная дял сохранения списка директориями
    
    while lst != []: # запускаем цикл для обхода папок
        print()
        print("ваш путь ",my_path)
        index = 1
        lst = [i for i in os.listdir(my_path) if os.path.isdir(my_path+i) ]  # формируем новый список с папками
        
        
        for i in lst:
            print(index," ",i)   # выводим на экран список директорий
            index += 1
           
        indx = input("Введите номер папки  или нажмите x чтобы сохранить в этой папке ")  # пользователь делает выбор
        
        if indx == "x" or index == "":
            break
        try:
            
            my_path += str(lst[int(indx) - 1])+'\\'  # формируем новый путь на основе выбора 
        except:
            print("ВВЕДИТЕ ЧИСЛО ИЛИ х, ПОЖАЛУЙСТА")
      
       
    # name_files = input("Введите имя файла с расширением ")

    # my_path += name_files
    # return my_path


def search():
    """ функция для поиска строки по слову, которое ввел пользователь
    """
    print("Список файлов для поиска ")
    
    lst_files = [i for i in os.listdir() if os.path.isfile(i)]    # список который содержит файлы
    
    print_dir()
   
    indx = input("Введите номер файла или  х чтобы выйти ")  # пользователь делает выбор
    
    if indx == "x":
        return
    try:
        with open(lst_files[int(indx)-1],encoding="utf-8") as f: # Читаем файл 
            txt = f.readlines()   # содержимое файла сохраняем в виде списка
            
        search_word = input("Введите слова для поиск ")   # просим ввести слово для поиска
        
        for i in txt:                      # производим поиск строки, где содержится слово
            if search_word in i: 
                print(i)

    except:
        return

def modi_lines():
    """ Функция для замены слова в текстовом файле
    """
    try:
        print("Список файлов для чтения ")
        lst_files = [i for i in os.listdir() if os.path.isfile(i)]   # список который содержит файлы
        
        print(*lst_files,sep="|")            # вывод файлов 
        
        file = input("Введите имя файла или  х чтобы выйти ")   # пользоваетль вводит имя файла
        if file not in lst_files:                          # проверяем есть ли такой файл
            print("НЕТ такого файла желаете создать?")    #  если нет, то предлагаем создать
            ch = input("Введите yes или no ")             
            if ch == "yes":                   
                add_new()
            else:
                return

        if file == "x":        
            return
        
        with open(file,encoding="utf-8") as f:      #  читаем выбранный файл
            txt = f.readlines()          #  сохраняем в переменную список
        index = 1
        
        while index <= len(txt):                # выводим  строкм на экран 
            print(index," ",txt[index-1][:],sep="") 
            index +=1
        modi_index = int(input("Введите номер строки которую вы измнить "))   # пользоваетль вводит номер строки
        
        if 1<= modi_index <= index :
            new_line = txt[modi_index-1].split()              # разбиваем строку на отдельные слова
            indx = 1
            
            for i in range(len(new_line)):                   # выводим слова на экран
                print(indx, " ",new_line[i])
                indx += 1
                
            user_index = int(input("Введите номер слова,которое вы хотите изменить "))    # пользователь выирает слово
            
            if 1 <= user_index <= indx:
                word = input("Введите новый текст ")           # пользователь вводит слово
                new_line[user_index-1] = word                   # меняем старое слово на новое
            
            with open(file,"w",encoding="utf-8") as f:       # перезаписываем файл с новым словом 
                #del txt[modi_index-1]
                txt[modi_index-1] = " ".join(new_line)+"\n"
                f.writelines(txt)
        else:
            print("неккоректный ввод индекса")
    except:
        print("Неккоректный ввод")
        return


def remove_lines():
    """ Функция для удаления строки в текстовом файле
    """
    try:
        print("Список файлов для чтения ")
        lst_files = [i for i in os.listdir() if os.path.isfile(i)]       # список который содержит файлы
        
        print_dir()                       # вывод файлов
        
        file = input("Введите имя файла или  х чтобы выйти ")           # пользоваетль вводит имя файла
        
        if file == "x":
            return
        
        with open(file,encoding="utf-8") as f:                 #  читаем выбранный файл
            txt = f.readlines()                                 #  сохраняем все ввиде списка
            
        index = 1
        
        while index <= len(txt):
            print(index," ",txt[index-1][2:],sep="")        #  выводим строки на экран
            index +=1
            
        remove_index = int(input("Введите номер строки которую вы хотете удалить"))      #  пользователь выбирает строку
        
        if 1<= remove_index <= index:
            txt.pop(remove_index-1)           # удаляем выбранную строку 
            
            with open(file,"w",encoding="utf-8") as f:       # перезаписываем файл без строки 
                f.writelines(txt)
        else:
            print("неккоректный ввод индекса")
    except:
        return
    

def remove_file():
    """ функция для удаления файла
    """
    print("Вам не кажется что у вас много файлов?")
    print("Давайте что-нибудь удалим")
    print("Список файлов: ",*os.listdir()) # список который содержит файлы 
    file_name = input("Введите имя файла или NO для отмены ")    # пользоваетль вводит имя файла
    if os.path.isfile(file_name):                      
        os.remove(file_name)                   # удаляем файл
    if file_name == 'x':
        return
    

def show_all() -> None:
    """ Данная функция читает файлы
    """
    print("Список файлов для чтения")
    lst_files = [i for i in os.listdir() if os.path.isfile(i)]     # Список файлов   
                     
    print_dir()
    
    while True:
        indx = input("Введите номер файла или  х чтобы выйти ")
        if indx == "x":
            break
        try:
            with open(lst_files[int(indx)-1],encoding="utf-8") as f:            # читаем файл и выводим на экран
                print(f.read())
        except:
            print("Такого файла нет или произошла ошибка")
            print()
            print("Чтобы выйти нажмите х")
            
    

def  add_new():
    """ функция создает новые файлы или добавляет в существующие новый текст
    """
    print("Введите имя файла куда нужно сохранить данные (с расширением )")
    file_name = input()             # выводим  имя файла
    if os.path.isfile(file_name):    # если файл такой есть то добавляем новую запись
        with open(file_name,"a",encoding="utf-8") as f:
            last_name =input("Введите фамилию ")
            first_name = input("введите имя ")
            patronymic = input("Введите отчество ")
            phone_number = input("Введите номер телефона ")
            f.write(f"{last_name} {first_name} {patronymic}  номер телефона - {phone_number}\n")
    else:
        with open(file_name,"w",encoding="utf-8") as f:           # если файл нет, то создаем новый
            f.write("\n")
            last_name =input("Введите фамилию ")
            first_name = input("введите имя ")
            patronymic = input("Введите отчество ")
            phone_number = input("Введите номер телефона ")
            f.write(f"{last_name} {first_name} {patronymic}: номер телефона - {phone_number}\n")
    
    
def main():
    while True:
        print("1 - показать все записи")
        print("2 - добавить запись")
        print("3 - чтобы удалить файл")
        print("4 - Удалить запись")
        print("5 - чтобы изменить запись")
        print("6 - поиск")
        print("7 - чтобы просмотрерть все папки")
        print("8 - чтобы скопировать содержимое файла")
        answer = input("Введите операцию или 0 для выхода ")
        
        if answer == "1":
            show_all()
        elif answer == "2":
            add_new()
        elif answer == "3":
            remove_file()  
        elif answer == "4":
            remove_lines()  
        elif answer == "5":
            modi_lines()
        elif answer == "6":
            search()
        elif answer == '7':
            choice_dir()
        elif answer == "8":
            coppy_lines()
        if answer == "0":
            exit()

      


if __name__ == "__main__":
    main()