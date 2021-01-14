x = input('Enter number: ')
try:
    x_number = int(x)
    if x_number > 0:
        second_number = int(x + x)
        third_number = int(x + x + x)
        sum = x_number + second_number + third_number
    else: #для отрицательных чисел изменяем их на положительное, делаем все что в if и меняем знак суммы
        x_number = x_number * (-1)
        x = str((-1) * int(x))
        second_number = int(x + x)
        third_number = int(x + x + x)
        sum = x_number + second_number + third_number
        sum = sum * ( -1 )
    print('Sum: ' , sum)
except ValueError:
    print('error, enter number')