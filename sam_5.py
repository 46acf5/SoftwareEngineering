def find_substring_in_list(substring, string_list):
    # Ищем строки, содержащие подстроку, и возвращаем новый список
    result = [s for s in string_list if substring in s]
    return result

list_of_strings = ["apple", "banana", "cherry", "grape", "pineapple"]
substring = "app"
print(find_substring_in_list(substring, list_of_strings))  

list_of_strings = ["hello", "world", "python", "programming", "chat"]
substring = "o"
print(find_substring_in_list(substring, list_of_strings))  

list_of_strings = ["data", "science", "machine", "learning"]
substring = "ai"
print(find_substring_in_list(substring, list_of_strings)) 
