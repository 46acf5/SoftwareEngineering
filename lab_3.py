class Car:  #конструктор класса Car
    def __init__(self, make, model): #функция инициализации машины с параметрами
        # бренда и модели
        self.make = make #инициализация бренда
        self.model = model #инициализация модели

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

my_car = Car("Toyota", "Corolla") # создание записи экземпляра машины
#бренда Toyota, модели Corolla
my_car.drive()

class ElectricCar (Car): # конструктор класса ElectricCar, наследующего класс Car
    def __init__(self, make, model, battery_capacity): # функция инициализации машины
        # с параметрами бренда, модели и мощности батареи
        super().__init__(make, model) # использование метода класса Car
        self.battery_capacity = battery_capacity # параметр ElectricCar вместимости батареи

    def charge(self): # функция, выводащая нужные данные
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

my_electric_car = ElectricCar ("Tesla", "Model S", 75) # конструктор
my_electric_car.drive() # метод, выводящий информацию об управляемой машине
my_electric_car.charge() #  метод, выводящий информацию о подзаправке
