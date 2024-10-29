class Car:  #конструктор класса Car
    def __init__(self, make, model): #функция инициализации машины с параметрами
        # бренда и модели
        self.make = make #инициализация бренда
        self.model = model #инициализация модели

my_car = Car("Toyota", "Corolla") #создание записи экземпляра машины
#бренда Toyota, модели Corolla
