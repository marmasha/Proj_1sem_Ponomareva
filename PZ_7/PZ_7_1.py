# Дана строка. Преобразовать в ней все строчные буквы (как латинские, так и русские)
# в прописные, а прописные — в строчные.

a = input('Введите строку: ') #  ввод данных с клавиатуры
a = a.swapcase() # возвращает копию строки с заглавными буквами, преобразованными в строчные и наоборот
print('Преобразованная строка:', a) # вывод данных на консоль
