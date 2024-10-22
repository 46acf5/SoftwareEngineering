![image](https://github.com/user-attachments/assets/89fa8b27-aaa0-4bc2-9eea-d4f2859d6129)# Тема 7 Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил(а):
+ Тимашева Алина Андреевна
+ ИВТ-22-2

| Задание | Лаб_раб | Сам_раб |
|--------:|---------|---------|
|Задание 1|+        |+        |
|Задание 2|+        |+        |
|Задание 3|+        |+        |
|Задание 4|+        |+        |
|Задание 5|+        |+        |
|Задание 6|+        |-        |
|Задание 7|+        |-        |
|Задание 8|+        |-        |
|Задание 9|+        |-        |
|Задание 10|+       |-        |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
+ к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### 
Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.

### Результат.
![image](https://github.com/user-attachments/assets/43945d02-babe-48af-b6ae-f94fbcfd6801)

## Выводы
В данном задании был создал тестовый файл input.txt для дальнейшей работы с ним.

## Лабораторная работа №2
### 
Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readline())
f.close()
```

### Результат.
![image](https://github.com/user-attachments/assets/f9309347-26b5-478d-8c40-703925e6162e)

## Выводы
В данном задании была изучена работа метода readline().

## Лабораторная работа №3
### 
Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```python
import codecs

f = open('input.txt', 'r', encoding='utf-8')
print(f.readlines())
f.close()
```

### Результат.
![image](https://github.com/user-attachments/assets/45f678f8-9527-47e4-a24e-f2a39d0828a4)

## Выводы
В данном задании была изучена работа метода readlines().
  
## Лабораторная работа №4
### 
Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```python
import codecs

with open('input.txt', encoding='utf-8') as f:
    for line in f:
        print(line)
```

### Результат.
![image](https://github.com/user-attachments/assets/a9335e36-7717-4e0b-bef1-8297876ac676)

## Выводы
В данном задании было изучено чтение файла построчно.

## Лабораторная работа №5
### 
Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
import codecs

with open('input.txt', encoding='utf-8') as f:
    print(f.readlines())
```

### Результат.
![image](https://github.com/user-attachments/assets/c22473c2-8393-43de-8b50-3036879729a3)

## Выводы
В данном задании была изучена работа конструкции with open().

## Лабораторная работа №6
### 
Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
import codecs

with open('input.txt', 'a+', encoding='utf-8') as f:
    f.write('\nIm additional line')

with open('input.txt', 'r', encoding='utf-8') as f:
    result = f.readlines()
    print(result)
```

### Результат.
![image](https://github.com/user-attachments/assets/b369e098-9f5e-428c-b390-5217e4bfc623)

## Выводы
В данном задании был изучен способ добавления новых строк в файл.

## Лабораторная работа №7
### 
Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.

```python
import codecs

lines = ['one', 'two', 'three']
with open('input.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        f.write('\nCycle run' + line)
    print('Done!')
```

### Результат.
![image](https://github.com/user-attachments/assets/63ca5fb6-7579-446c-8429-beaa866dc6c9)
![image](https://github.com/user-attachments/assets/b52ecc34-95cd-41c4-873b-ae98b327b92e)
![image](https://github.com/user-attachments/assets/26f5a608-5924-4d7d-9f96-aa8eb11636dd)

## Выводы
В данном задании был изучен способ изменения данных в файле.

## Лабораторная работа №8
### 
Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

```python
import os
from traceback import print_exc


def print_docs (directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print('Папка {catalog[8]} содержит:')
        print (f' Директории: {", ".join([folder for folder in catalog[1]])}')
        print (f'Файлы: {", ".join([file for file in catalog[2]])}')
        print('-' * 40)

print_docs("/Users/46acf/eclipse")
```

### Результат.
![image](https://github.com/user-attachments/assets/6c4848ed-86e7-4643-ae99-ad8d344e0229)
![image](https://github.com/user-attachments/assets/8bb0ff77-6e02-490f-9de3-544cf59a8ad2)

## Выводы
В данном задании была разработана функция print_docs(directory).

## Лабораторная работа №9
### 
Документ «input.txt» содержит следующий текст:

Приветствие

Спасибо

Извините

Пожалуйста

До свидания

Ты готов?

Как дела?

С днем рождения!

Удача!

Я тебя люблю.


Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных

```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words('input.txt'))
```

### Результат.
![image](https://github.com/user-attachments/assets/7b247816-b980-4974-b0d9-c096cc91bb68)

## Выводы
В данном задании были изучены способы подсчета длины слова и списка слов.

## Лабораторная работа №10
### 
Требуется создать csv-файл «rows_300.csv» со следующими столбцами: 
№ - номер по порядку (от 1 до 300); 
Секунда - текущая секунда на вашем ПК; 
Микросекунда текущая миллисекунда на часах.

Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды. 

```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['N', 'Секунда, Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second,
                         datetime.datetime.now().microsecond])
        time.sleep(0.01)
```

### Результат.
![image](https://github.com/user-attachments/assets/39cc0696-3b4b-4d0d-bb7d-84d1b68f04fb)
![image](https://github.com/user-attachments/assets/29424f2b-61b8-4e72-a8d4-b55f5069ab63)
![image](https://github.com/user-attachments/assets/2a682dfb-d72d-45bc-8ad8-a02700ea3d44)

## Выводы
В данном задании был изучен способ составления таблицы в текстовом файле, а также способ записи туда изменяющихся данных.

## Самостоятельная работа №1
### 
Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация. 

```python
from collections import Counter
import re


def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    # Удаление символов пунктуации
    words = re.findall(r'\b\w+\b', text)

    # Подсчет количества слов
    word_count = len(words)

    # Используем Counter для подсчета частоты слов
    word_freq = Counter(words)

    most_common_word, frequency = word_freq.most_common(1)[0]

    print(f"Общее количество слов: {word_count}")
    print(f"Самое частое слово: '{most_common_word}' встречается {frequency} раз(а)")


count_words('article.txt')
```

### Результат.
![image](https://github.com/user-attachments/assets/01314e39-d225-48a9-9f9c-e91ce1fd0946)
![image](https://github.com/user-attachments/assets/a90f73fe-3914-4f75-949a-dde749472fcc)

## Выводы
Первое задание помогло разобраться с работой файлов в Python и функцией Counter для подсчета частоты слов.

## Самостоятельная работа №2
### 
У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы. 

```python
with open('prices.txt') as f:
  print(sum(map(lambda x: int(x[1]) * int(x[2]), map(str.split, f.readlines()))))
```

### Результат.
![image](https://github.com/user-attachments/assets/7a992658-674e-4211-aac0-bb095a42bfb3)
![image](https://github.com/user-attachments/assets/5e9b2dbe-2ad7-4dc9-8460-8ec48844f135)

## Выводы
Второе задание продемонстрировало создание программы для учета расходов с использованием базовых функций записи и чтения файлов.
  
## Самостоятельная работа №3
### 
Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк. 

• Текст в файле: 
Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated. 

• Ожидаемый результат: Input file contains: 
108 letters 
20 words 
4 lines

```python
def file_statistics(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    num_lines = len(lines)
    num_letters = 0
    num_words = 0

    for line in lines:
        words = line.split()
        num_words += len(words)
        num_letters += sum(c.isalpha() for c in line)

    print(f"Input file contains:")
    print(f"{num_letters} letters")
    print(f"{num_words} words")
    print(f"{num_lines} lines")


file_statistics('input.txt')
```

### Результат.
![image](https://github.com/user-attachments/assets/2bb57e0f-9642-453c-8520-ad0fa5c12408)
![image](https://github.com/user-attachments/assets/03271743-8438-472d-bafd-5706fb28cf99)

## Выводы
Третье задание показало, как подсчитывать буквы, слова и строки в тексте с использованием простых операций обработки строк.
  
## Самостоятельная работа №4
### 
Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово ехат, то слова ехат, Exam, ExaM, ЕХАМ и ехАт должны быть заменены на ****. 

• Запрещенные слова: 
hello email python the exam wor is 

• Предложение для проверки: 
Hello, world! Python IS the programming language of the future. My EMAIL is.... 
PYTHON is awesome!!!! 

• Ожидаемый результат: 
*****, ***ld! ******  *** programming language of *** future. My ***** .... 
 ****** **.... awesome!!!! 

```python
import re

def load_forbidden_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        forbidden_words = file.read().split()
    return forbidden_words


def censor_text(text, forbidden_words):
    """Замена запрещенных слов на звездочки"""
    for word in forbidden_words:
        # Используем регулярные выражения для поиска слов независимо от регистра
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub('*' * len(word), text)
    return text


def main():
    # Загрузка запрещенных слов из файла
    forbidden_words = load_forbidden_words('input.txt')
    # Ввод предложения от пользователя
    input_text = input("Введите предложение: ")
    # Замена запрещенных слов
    censored_text = censor_text(input_text, forbidden_words)
    print(censored_text)

main()
```

### Результат.
![image](https://github.com/user-attachments/assets/69acbe0e-7b28-4f46-8f13-ef75b3b6a718)
![image](https://github.com/user-attachments/assets/f7ede352-f981-4e2f-b964-0e8571ee1669)

## Выводы
Шаги реализации:
1. Прочитать список запрещенных слов из файла.
2. Заменить эти слова в предложении на звездочки.
3. Вывести результат.

Задание 4 показало, как эффективно работать с текстом и заменять запрещенные слова, используя регулярные выражения для игнорирования регистра.
  
## Самостоятельная работа №5
### 
Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

Задача: Напишите программу, которая сохраняет информацию о любимых фильмах пользователя. Пользователь может добавлять новые фильмы в список, а также просматривать все фильмы, которые он добавил ранее.

```python
def add_film():
    """Добавление нового фильма в список"""
    film = input("Введите название фильма: ")
    with open('films.txt', 'a', encoding='utf-8') as file:
        file.write(f"{film}\n")
    print(f"Фильм '{film}' добавлен в список.")

def view_films():
    """Просмотр всех добавленных фильмов"""
    try:
        with open('films.txt', 'r', encoding='utf-8') as file:
            films = file.readlines()
            if films:
                print("\nСписок любимых фильмов:")
                for i, film in enumerate(films, 1):
                    print(f"{i}. {film.strip()}")
            else:
                print("Список фильмов пуст.")
    except FileNotFoundError:
        print("Файл с фильмами не найден.")

def main():
    while True:
        print("\n1. Добавить фильм")
        print("2. Просмотреть список фильмов")
        print("3. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            add_film()
        elif choice == '2':
            view_films()
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

main()

```

### Результат.

## Выводы
Задание 5 позволило понять, как можно взаимодействовать с текстовыми файлами для сохранения и вывода данных, что полезно при работе с файлами и простыми базами данных.
