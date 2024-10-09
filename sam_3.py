from collections import Counter

def top_numbers(number_string):
    # Преобразуем строку в список целых чисел
    number_list = [int(num) for num in number_string]
    # Используем Counter для подсчета количества вхождений каждого числа
    count = Counter(number_list)
    # Получаем три самых частых числа
    most_common = count.most_common(3)
    # Преобразуем список самых частых в словарь
    result_dict = dict(most_common)
    # Сортируем словарь по ключам (по возрастанию)
    sorted_result = dict(sorted(result_dict.items()))
    # Возвращаем отсортированный словарь
    return sorted_result

number_string = "555123456789000123456789123"
result = top_numbers(number_string)

print(result)
