def my_func(x, y):
    return x ** (y)


result = my_func(x=int(input('Enter X: ')), y=int(input('Enter Y: ')))
print(result)


def my_func_2(x, y):
    z = x
    while y < -1:
        z = z * x
        y = y + 1
    return 1 / z


result = my_func_2(x=int(input('Enter X: ')), y=int(input('Enter Y: ')))
print(result)
