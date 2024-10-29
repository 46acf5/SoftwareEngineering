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
