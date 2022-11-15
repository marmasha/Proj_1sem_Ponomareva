# Дан список размера N, все элементы которого, кроме первого, упорядочены по
# возрастанию. Сделать список упорядоченным, переместив первый элемент на новую
# позицию.

from random import randint # библиотека дает возможность генерировать случайные числа
print('Введите размер списка:')
a = [randint(1, 100) for i in range(int(input(''))) ]
print('Список:', a) # вывод данных на консоль
a.sort() #  сортирует все элементы по возрастанию
print('Упорядоченный список:', a) # вывод данных на консоль
a += [a.pop(0)] # перемещает первый элемент на новую позицию
print('Упорядоченный список с перемещённым элементом:', a) # вывод данных на консоль
