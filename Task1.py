def division(num_1, num_2):
    try:
        print('Результат деления: ', num_1 / num_2)
    except ZeroDivisionError:
        print('Second number is 0')

num_1 = float(input('Enter number 1: '))
num_2 = float(input('Enter number 2: '))
division(num_1, num_2)