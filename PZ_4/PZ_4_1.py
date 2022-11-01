def factorial(num: int) -> int:  # Функция для нахождения факториала
    factorial = 1
    for i in range(2, num + 1): # Задаёт значения индексной переменной
        factorial *= i
    return factorial #Возвращает данные после выполнения работы самой функции

try: # Обработчик исключений
    x = float(input("Введите x: ")) # Ввод данных с клавиатуры
    n = int(input("Введите n: "))  # Ввод данных с клавиатуры

    count = 1 # Подсчитывает количество записей, возвращенных запросом
    result = 1 + x

    if n > 0:
        while count <= n:
            result += x ** count / factorial(count)  # Формула, которая решает данную задачу
            count += 1

        print(result)  # Вывод приближенного значения

except Exception as ex:
    print(ex)