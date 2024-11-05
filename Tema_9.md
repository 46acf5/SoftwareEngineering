# Тема 9. Концепции и принципы ООП
Отчет по Теме #9 выполнил(а):
+ Тимашева Алина Андреевна
+ ИВТ-22-2

| Задание | Лаб_раб | Сам_раб |
|--------:|---------|---------|
|Задание 1|+        |+        |
|Задание 2|+        |-        |
|Задание 3|+        |-        |
|Задание 4|+        |-        |
|Задание 5|+        |-        |
|Задание 6|-        |-        |
|Задание 7|-        |-        |
|Задание 8|-        |-        |
|Задание 9|-        |-        |
|Задание 10|-       |-        |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
+ к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### 


```python
class Ivan:
    __slots = ['name']

    def __init__(self, name):

        if name == 'Иван':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Иван"

person1 = Ivan ('Алексей')
person2 = Ivan ('Иван')
print(person1.name)
print(person2.name)

person2.surname = 'Петров'
```

### Результат.

## Выводы


## Лабораторная работа №2
### 


```python
class Icecream:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def composition(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient}")
        else:
            print('Обычное мороженое')

icecream = Icecream()
icecream.composition()
icecream = Icecream ('шоколадом')
icecream.composition()
icecream = Icecream(5)
icecream.composition()
```

### Результат.

## Выводы

## Лабораторная работа №3
### 


```python
class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value): # установка значения атрибута
        self._value = value

    def get_value(self): # получение значения атрибута
        return self._value

    def del_value (self): # удаление атрибута
        del self._value

    value = property(get_value, set_value, del_value, "Свойство value")


obj = MyClass (42)
print(obj.get_value())
obj.set_value (45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value()
print(obj.get_value())
```

### Результат.

## Выводы

  
## Лабораторная работа №4
### 


```python
class Mammal:
    className = 'Mammal'

class Dog (Mammal):
    species = 'canine'
    sounds = 'wow'

class Cat (Mammal):
    species = 'feline'
    sounds = 'meow'

dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds}")
cat = Cat()
print(f"Cat is {cat.className}, but they say {cat.sounds}")
```

### Результат.

## Выводы


## Лабораторная работа №5
### 


```python
class Russian:
    @staticmethod
    def greeting():
        print("Привет")

class English:
    @staticmethod
    def greeting():
        print("Hello")

def greet(language):
    language.greeting()

ivan = Russian()
greet(ivan)
john = English()
greet(john)
```

### Результат.

## Выводы


## Самостоятельная работа №1
### 


```python

```

### Результат.

## Выводы
