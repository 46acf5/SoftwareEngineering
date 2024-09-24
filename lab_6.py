string = 'Hello all students!'
value = input()
for i in string:
    if i == value:
        index = string.find(value)
        print(f'Letter {value} presents in the proposal with {index} index')
        break
else: print(f'Letter {value} does not present in the proposal')
