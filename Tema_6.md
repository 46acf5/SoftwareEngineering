# Тема 6 Базовые коллекции: словари, кортежи
Отчет по Теме #6 выполнил(а):
+ Тимашева Алина Андреевна
+ ИВТ-22-2

| Задание | Лаб_раб | Сам_раб |
|--------:|---------|---------|
|Задание 1|+        |+        |
|Задание 2|+        |+        |
|Задание 3|+        |+        |
|Задание 4|+        |+        |
|Задание 5|+        |+        |
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
request = int(input('Введите номер кабинета: '))

dictionary = {
    101: {'key': 1234, 'access': True},
    102: {'key': 1337, 'access': True},
    103: {'key': 8943, 'access': True},
    104: {'key': 5555, 'access': False},
    None: {'key': None, 'access': False},
}

response = dictionary.get(request)
if not response:
    response = dictionary [None]
key = response.get('key')
access = response.get('access')
print(key, access)
```

### Результат.

## Выводы


## Лабораторная работа №2
### 


```python
from pprint import pprint

my_dict={'first': 'so easy'}

def dict_maker (**kwargs):
    my_dict.update(**kwargs)

dict_maker (a1 = 1, a2 = 20, a3 = 54, a4 = 13)
dict_maker(name="Михаил", age = 31, weight = 70, eyes_color='blue')
pprint(my_dict)
```

### Результат.

## Выводы

## Лабораторная работа №3
### 


```python
input_string = 'HelloWorld'
result = tuple(input_string)
print(result)
print(list(result))
```

### Результат.

## Выводы

  
## Лабораторная работа №4
### 


```python
def personal_info(name, age, company='unnamed'):
    print(f"Имя: {name} Возраст: {age} Компания: {company}")

tom = ("Григорий", 22)
personal_info(*tom)

bob = ("Георгий", 41, "Yandex")
personal_info(*bob)
```

### Результат.

## Выводы


## Лабораторная работа №5
### 


```python
def tuple_sort(tpl):
    for elm in tpl:
        if not isinstance(elm, int):
            return tpl
    return tuple(sorted(tpl))

if __name__ == '__main__':
    print(tuple_sort((5, 5, 3, 1, 9)))
    print (tuple_sort((5, 5, 2.1, '1', 9)))
```

### Результат.

## Выводы


## Самостоятельная работа №1
### 


```python

```

### Результат.

## Выводы

## Самостоятельная работа №2
### 


```python

```

### Результат.

## Выводы

  
## Самостоятельная работа №3
### 


```python

```

### Результат.

## Выводы

  
## Самостоятельная работа №4
### 


```python

```

### Результат.

## Выводы

  
## Самостоятельная работа №5
### 


```python

```

### Результат.

## Выводы
