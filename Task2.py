list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for i, el in enumerate(list) if list[i] > list[i - 1]]
print(new_list)
