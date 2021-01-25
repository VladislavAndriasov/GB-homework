import math
from itertools import count


def fact(n):
    temp = math.factorial(n)
    yield temp


n = int(input("Enter number:"))
for el in fact(n):
    print(el)
