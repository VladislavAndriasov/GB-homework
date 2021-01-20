def my_func(num_1, num_2, num_3):
    temp = min(num_1, num_2, num_3)
    if temp == num_1:
        result = num_2 + num_3
    elif temp == num_2:
        result = num_1 + num_3
    else:
        result = num_1 + num_2
    print(result)


my_func(num_1=float(input('Enter number 1: ')),
        num_2=float(input('Enter number 2: ')),
        num_3=float(input('Enter number 3: ')))
