my_list = input('Enter elements in list separated by a space : ').split()
element = len(my_list)
i = 0
while i < element:
    temp = my_list.pop(i)
    my_list.insert(i + 1, temp)
    i += 2
print(my_list)