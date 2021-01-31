with open('test.txt') as text:
    temp = []
    str_num = 0.0
    a = 0
    for i in enumerate(text):
        i = list(i)
        i.pop(0)
        for u in i:
            y = u.split()
            temp.append(float(y[1]))
            for t in temp:
                str_num += t
                a += 1
            if float(y[1]) > 20000:
                print(y[0])
    print(str_num / a)
