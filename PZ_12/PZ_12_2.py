# Вариант 18
# Составить генератор (yield), который преобразует все буквенные символы в
# строчные

def lowercase_generator(text):
    for char in text:
        if char.isalpha():
            yield char.lower()
        else:
            yield char

text = "Hello, World! I am HaPpY:)"
result = "".join(lowercase_generator(text))
print(result) 
