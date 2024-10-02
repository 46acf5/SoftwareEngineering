def replace(input_list):
    a = input_list[0]
    input_list[0] = max(input_list)
    input_list[len(input_list)-1] = a

    return input_list

print(replace([1,2,3,4,5]))
