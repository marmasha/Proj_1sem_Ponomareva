# Из предложенного текстового файла (text18-18.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме выведя строки в обратном порядке.

import string

with open('text18-18.txt', 'r', encoding='utf-8') as file_text:
    file_read = file_text.read()
    file_readlines = file_read.split('\n')

print('Содержимое:', file_read, '\n\nКоличество символов:', len(file_read), '\n')

# Подсчет знаков пунктуации в первых четырех строках
punctuation_count = 0
for i, line in enumerate(file_readlines[:4]):
    punctuation_count += sum(1 for char in line if char in string.punctuation)

print('Количество знаков пунктуации в первых четырех строках:', punctuation_count)

# Формирование нового файла с текстом в стихотворной форме
reversed_lines = reversed(file_readlines)
new_text = '\n'.join(reversed_lines)

with open('new_file.txt', 'w', encoding='utf-8') as file_new_text:
    file_new_text.write(new_text)

print("Файл 'new_file.txt' успешно создан с текстом в стихотворной форме.")