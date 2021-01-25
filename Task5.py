from functools import reduce

my_set = {el for el in range(99, 1001) if el % 2 == 0}


def my_f(num1, num2):
    return num1 * num2


print(reduce(my_f, my_set))
