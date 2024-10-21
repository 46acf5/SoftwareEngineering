import codecs

with open('input.txt', 'a+', encoding='utf-8') as f:
    f.write('\nIm additional line')

with open('input.txt', 'r', encoding='utf-8') as f:
    result = f.readlines()
    print(result)
