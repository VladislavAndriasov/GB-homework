time = input('Enter time in seconds: ')
try: #проверка введено ли действительно число, заданием не подразумевается иное, но посмотрел как это проверять в интернете
    correct_time = int(time)
    if correct_time > 0:
        time_in_hours = correct_time // 3600
        correct_time = correct_time - time_in_hours * 3600
        time_in_seconds = correct_time // 60
        correct_time = correct_time - time_in_seconds * 60
        print(f'{time_in_hours} : {time_in_seconds} : {correct_time}')
    else:
        print('error, enter a positive number')
except ValueError:
    print('error, enter number')

