x = input('Enter number: ')
highest_digit = 0
try:
    number = int(x)
    if number > 0:
        while number > 0:
            first_number = number % 10
            second_number = number % 100 // 10
            if first_number > highest_digit:
                highest_digit = first_number
            elif second_number > highest_digit:
                highest_digit = second_number
            number = number // 10
        print('The biggest digit in the number is: ', highest_digit)
    else:
        print('Enter positive number')
except ValueError:
    print('Error, enter number')