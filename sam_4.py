def find_entry_exit(sequence, employee_id):
  
    if employee_id not in sequence:
        return tuple()

    first_index = sequence.index(employee_id)
  
    try:
        second_index = sequence.index(employee_id, first_index + 1)
        return sequence[first_index:second_index + 1]
    except ValueError:
        return sequence[first_index:]

print(find_entry_exit((1, 2, 3), 8))
print(find_entry_exit((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(find_entry_exit((1, 2, 8, 5, 1, 2, 9), 8))
