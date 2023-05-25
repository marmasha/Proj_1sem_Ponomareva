# Блок 2, вариант 18
# Создание базового класса "Транспортное средство" и его наследование для создания
# классов "Автомобиль" и "Мотоцикл". В классе "Транспортное средство" будут
# общие свойства, такие как максимальная скорость и количество колес, а классы-
# наследники будут иметь свои уникальные свойства и методы.

class Transport:
    def __init__(self, max_speed, wheels):
        self.max_speed = max_speed
        self.wheels = wheels

class Car(Transport):
    def __init__(self, max_speed, wheels, brand, model):
        super().__init__(max_speed, wheels)
        self.brand = brand
        self.model = model
        self.fuel = 0

    def drive(self, distance):
        fuel_consumption = distance / 10.0
        if fuel_consumption <= self.fuel:
            self.fuel -= fuel_consumption
            return f"{self.brand} {self.model} проехал {distance}km"
        else:
            return "Недостаточно топлива"

    def add_fuel(self, amount):
        self.fuel += amount

class Motorcycle(Transport):
    def __init__(self, max_speed, wheels, brand, model, helmet):
        super().__init__(max_speed, wheels)
        self.brand = brand
        self.model = model
        self.helmet = helmet

    def wear_helmet(self):
        return f"{self.brand} {self.model} носит {self.helmet}"

# Пример использования классов
car = Car(200, 4, "Toyota", "Camry")
print(car.drive(50)) # Недостаточно топлива
car.add_fuel(10)
print(car.drive(50)) # Toyota Camry проехал 50km

motorcycle = Motorcycle(150, 2, "Honda", "CBR", "полную защиту")
print(motorcycle.wear_helmet()) # Honda CBR носит полную защиту