# Дано число R и список размера N. Найти два различных элемента списка, сумма
# которых наиболее близка к числу R, и вывести эти элементы в порядке возрастания
# их индексов (определение наиболее близких чисел - то есть такой элемент AK, для
# которого величина |AK - R| является минимальной).

from random import randint
r = int(input('Введите число R:')) #  ввод данных с клавиатуры
n = int(input('Введите размер списка:')) #  ввод данных с клавиатуры
a = [randint(1, 100) for i in range(n) ] #  заполнение списка
print('Список:', a) # вывод данных на консоль
min = abs(r - (a[0] + a[1])) #  Минимальное обозначение суммы элементов
i_m = 1
for i in range(n): #  вычисление суммы и нахождение элементов близких к R
    d = abs(r - (a[i-1] + a[i]))
    if min > d:
      min = d
      i_m = i
if a.index(a[i_m-1]) < a.index(a[i_m]): # вывод элементов в порядке возрастания
  print('Элементы, сумма которых близка к R:', a[i_m-1], (a[i_m])) # вывод данных на консоль
else:
  print('Элементы, сумма которых близка к R:', a[i_m], (a[i_m-1])) # вывод данных на консоль