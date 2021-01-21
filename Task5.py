my_list = [7, 5, 3, 3, 2]
element = len(my_list)
i = 0
entered_by_user = int(input('Enter number: '))
if my_list.count(entered_by_user):
    pos = my_list.index(entered_by_user)
    my_list.insert(pos + 1, entered_by_user)
else:
    while  i < element:
        temp = (my_list[i])
        if temp > entered_by_user:
            i += 1
        else:
            my_list.insert(i, entered_by_user)
            break
    else:
        my_list.append(entered_by_user)
print(my_list)



