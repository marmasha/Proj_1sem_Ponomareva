import random # библиотека дает возможность генерировать случайные числа

# функция позволяет разложить четырехзначное число
def array(x):
    nums = []
    while x > 0:
        b = x % 10
        nums.append(b) # добавляет значение в конец списка
        x //= 10
    return list(reversed(nums)) # Перестраивает элементы списка в обратном порядке

x = random.randint(999, 10000) # генерирует четырехзнначное число
print('Четырехзначное число:', x) # вывод данных на консоль
a = array(x)
print('Есть одинаковые цифры' if len(set(a)) != len(a) else 'Нет одинаковых цифр')
