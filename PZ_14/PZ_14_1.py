#  Из исходного текстового файла (expansion.txt) выбрать имена фалов,
# соответствующие типам: .xls, .xml, .html, .css, .py.Посчитать количество полученных
# элементов.

import re

# Открываем файл и считываем его содержимое
with open('expansion.txt', 'r') as file:
    text = file.read()

# Используем регулярное выражение для поиска имен файлов
pattern = r'\b\w+\.(xls|xml|html|css|py)\b'
matches = re.findall(pattern, text)

# Выводим количество найденных элементов
print("Количество найденных элементов: ", len(matches))