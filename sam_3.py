from collections import Counter

def top_numbers(number_string):
    
    number_list = [int(num) for num in number_string]
    count = Counter(number_list)
    most_common = count.most_common(3)
    
    result_dict = dict(most_common)
    sorted_result = dict(sorted(result_dict.items()))
    return sorted_result

number_string = "555123456789000123456789123"
result = top_numbers(number_string)

print(result)
