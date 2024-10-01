def calcargs(*args):
    if args:
        average = sum(args)/len(args)
        return average
    else:
        return 0

if __name__ == '__main__':
    result = calcargs(11,22,33,44)
    print(f"Среднее арифметическое: {result}")
