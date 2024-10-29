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
