'''class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.current += 1
        return result


# Создаем объект итератора для получения первых 10 чисел Фибоначчи
fib_iter = FibonacciIterator(10)

# Итерация и вывод чисел Фибоначчи
for num in fib_iter:
    print(num)'''

'''# Открываем файл для чтения
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip()) #stripQ используется для удаления символа новой строки

# Файл автоматически закрывается при выходе из блока with'''

'''numbers = [0, 1, 2, 3, 4, 5]
for item in numbers:
    print(item)'''

'''class CountDown:
    def __init__(self, start):
        self.count = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count < 0:
            raise StopIteration
        return self.count

if __name__ == '__main__':
    counter = CountDown(5)
    for i in counter:
        print(i)'''

'''a = [i** 2 for i in range(1, 5)]

print('a', a)
for i in a:
    print(i)

print('iter(a) - ', iter(a))
for i in a:
    print(i)'''

'''b = (i ** 2 for i in range(1, 5))
print(b)
print('first')
for i in b:
    print(i)
print('second')

for i in b:
    print(i)'''

'''def countdown(count):
    while count >= 0:
        yield count
        count -= 1

if __name__ == '__main__':
    counter = countdown(5)
    for i in counter:
        print(i)'''


'''def fib(n):
    prev1 = 1
    prev2 = 1
    current = None
    yield 1
    if n > 1:
        yield 1
        for i in range(n - 2):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            yield current

if __name__ == "__main__":
    for i in fib(200):
        print(i)'''

'''def fib(n):
    prev1 = 1
    prev2 = 1
    current = None
    yield 1
    if n > 1:
        yield 1
        for i in range(n - 2):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            yield current

if __name__ == "__main__":
    with open("fib.txt", "w") as f:
        for i in fib(200):
            f.write(str(i) + "\n")'''
