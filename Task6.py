from itertools import count, cycle
for el in count(3):
    if el > 15:
        break
    else:
        print(el)

list = [1, 2, 3]
c = int(len(list))
for el in cycle(list):
    if c > 11:
        break
    print(el)
    c += 1