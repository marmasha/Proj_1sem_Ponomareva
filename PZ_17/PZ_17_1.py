# Блок 1, вариант 18
# Создайте класс "круг", который имеет атрибут радиуса и
# методы для вычисления площади, длины окружности и диаметра.

import math

class Circle:
    def __init__ (self, radius):
        self.radius = radius

    def r(self):
        self.r = self.radius
        return self.r

    def one(self):
        self.sqrt = (self.radius * self.radius)*3.14
        return self.sqrt
    def two(self):
        self.d =  (self.radius * 2)
        return self.d
    def three(self):
        self.dlina = (self.d * 3.14)
        return self.dlina
        
CircleOne = Circle(3)
print ('Радиус =', CircleOne.r())
print ('Площадь =', CircleOne.one())
print ('Диаметр =', CircleOne.two())
print ('Длина окружности =', CircleOne.three())