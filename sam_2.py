x = "hello world"
for i in range (len(x)):
    print (x[i])

one = int(input("Введите значение переменной: "))
if 0 < one <= 3:
    print("Переменная больше 0 и меньше 4")
    if 3 < one <= 6:
        print("Переменная больше 3 и меньше 7")
elif 6 < one <= 10:
    print("Переменная больше 6 и меньше 11")
else: print ("Ошибка ввода")
