list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for i, el in enumerate(list) if list[i] != list[i - 1]]
print(new_list)