import random
n: int = 0

def main():
    global n

    while True:
        a = random.randint(1,6)

        if a == 5 or a == 6:
            n += 1
            print(f"Попытка номер {n}. Выпало значение {a}! Вы победили!")
            break

        elif a == 3 or a == 4:
            n += 1
            continue

        else:
            n += 1
            print(f"Попытка номер {n}. Выпало значение {a}! Вы проиграли!")
            break

if name == 'main':
    main()
