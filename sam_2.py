with open('prices.txt') as f:
  print(sum(map(lambda x: int(x[1]) * int(x[2]), map(str.split, f.readlines()))))
