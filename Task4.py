my_list = input('Enter elements separated by a space : ').split()
for ind, el in enumerate(my_list, start = 1):
    print(ind, el[0:10:1])
