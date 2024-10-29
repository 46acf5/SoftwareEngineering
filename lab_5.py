class Shape: # инструкция «ничего не делать». Инструкция pass помогает
    # оформить ключевые конструкции, а потом вернуться к деталям.
    def area(self): # функция, определяющая фигуру для дальнейшей работы с ней
        pass

class Rectangle (Shape): # конструктор класса Rectangle
    def __init__(self, width, height): # функция, устанавливающая параметры прямоугольника
        self.width = width # ширина прямоугольника
        self.height = height # высота прямоугольника

    def area(self): # функция, возвращающая площадь прямоугольника
        return self.width * self.height

class Circle (Shape): # конструктор класса Circle
    def __init__(self, radius): # функция, устанавливающая параметры фигуры круг
        self.radius = radius # радиус круга

    def area(self): # функция, возвращающая площадь круга
        return 3.14 * self.radius * self.radius

shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(shape.area())
