#Имеется список студентов группы, в котором все имена различны. Определить, есть ли в
#группе студент, который побывал в гостях у всех студентов. (Для каждого студента
#составить список из множества побывавших у него в гостях друзей, причем хозяина в этот
#список не включать).

try: # обработчик исключений
    a = {"Катя", "Рома", "Петя", "Араш", "Диана"} # список студентов группы

    K = {"Рома", "Араш", "Диана"} # список побывавших в гостях у Кати
    R = {"Араш", "Петя", "Катя"} # список побывавших в гостях у Ромы
    P = {"Катя", "Рома", "Диана"} # список побывавших в гостях у Пети
    A = {"Петя", "Катя"} # список побывавших в гостях у Араша
    D = {"Катя"} # список побывавших в гостях у Дианы

    print("Человек, который побывал в гостях у всех студентов:", a & R & P & A & D) # вывод данных на консоль
except:
    print('error') # вывод данных на консоль