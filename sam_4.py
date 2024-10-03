def change(input_list):
    for i in range(len(input_list)):
        if input_list[i] == 3:
            input_list[i] = 4

    input_list[:] = [i for i in input_list if i != 2]

def main():
    one = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
    two = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
    three = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

    change(one)
    change(two)
    change(three)

    print(one)
    print(two)
    print(three)

if __name__ == "__main__":
    main()
