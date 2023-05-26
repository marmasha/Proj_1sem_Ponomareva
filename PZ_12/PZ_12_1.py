# Вариант 18
# В последовательности на n целых элементов найти произведение 
# элементов средней трети.

def multiply_middle_third(sequence):
    n = len(sequence)
    third = n // 3 * 2 # определяем количество элементов в средней трети
    start = (n - third) // 2 # определяем индекс начала средней трети
    end = start + third # определяем индекс конца средней трети
    result = 1 # инициализируем результат
    for i in range(start, end): # проходим по элементам средней трети
        result *= sequence[i] # вычисляем произведение элементов
    return result # возвращаем результат

sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #средней третью является [3, 4, 5, 6, 7, 8]
result = multiply_middle_third(sequence)
print(result) # выводим результат который равен 20160
