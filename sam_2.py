def remove_first_occurrence(tup, value):
    temp_list = list(tup)
    if value in temp_list:
        temp_list.remove(value)  # Удаляем только первое вхождение
    return tuple(temp_list)

print(remove_first_occurrence((1, 2, 3), 1))
print(remove_first_occurrence((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2),
                              3))
print(remove_first_occurrence((2, 4, 6, 6, 4, 2), 9))
