decision = input('Do you wish to work with list or dict? (type "list" or "dict"): ')
if decision == 'list':
    month_number = int(input('Enter month number: '))
    winter_list = [1, 2, 12]
    spring_list = [3, 4, 5]
    summer_list = [6, 7, 8]
    autumn_list = [9, 10, 11]
    if winter_list.count(month_number):
        print('The month refers to winter')
    elif spring_list.count(month_number):
        print('The month refers to spring')
    elif summer_list.count(month_number):
        print('The month refers to spring')
    elif autumn_list.count(month_number):
        print('The month refers to autumn')
    else:
        print('Incorrect number, enter number from 1 to 12')
elif decision == 'dict':
    month_dict = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring',
                  6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Autumn',
                  10: 'Autumn', 11: 'Autumn', 12: 'Winter'}
    month_number = int(input('Enter month number: '))
    print('The month refers to ', month_dict[month_number])
else:
    print('Incorrect, enter "list" or "dict"')
