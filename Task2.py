with open('test.txt') as text:
    string_num = 0
    for i in enumerate(text):
        i = list(i)
        string_num += 1
        i.pop(0)
        for u in i:
            y = u.split()
            o = len(y)
            print(f'Длина {string_num} строки {o}')
    print(f'Кол-во строк: {string_num}')
