def list_to_set(input_list):
    result_set = set()

    for num in set(input_list):
        count = input_list.count(num)

        result_set.add(num)

        for i in range(2, count + 1):
            result_set.add(str(num) * i)

    return result_set


def main():
    list_1 = [1, 1, 3, 3, 1]
    list_2 = [5, 5, 5, 5, 5, 5, 5]
    list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

    print(list_to_set(list_1))
    print(list_to_set(list_2))
    print(list_to_set(list_3))


if __name__ == '__main__':
    main()
