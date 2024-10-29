class Car: # конструктор класса Car
    def __init__(self, make, model):# функция инициализации машины
        # с параметрами бренда и модели
        self._make = make # Защищенный атрибут
        self.__model = model # Приватный атрибут

    def drive(self): # метод, выводящий информацию об управляемой машине
        print(f"Driving the {self._make} {self.__model}")

my_car = Car("Toyota", "Corolla") # создание экземпляра машины
print(my_car._make) # Доступ к защищенному атрибуту
#print(my_car__model) # Ошибка! Приватный атрибут недоступен
my_car.drive() # метод, выводящий информацию об управляемой машине
