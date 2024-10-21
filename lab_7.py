import codecs

lines = ['one', 'two', 'three']
with open('input.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        f.write('\nCycle run' + line)
    print('Done!')
