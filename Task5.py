with open('test.txt', 'w', encoding='utf-8') as text:
    line = input('Введите цифры через пробел \n')
    text.writelines(line)
    my_numb = line.split()
    print(sum(map(int, my_numb)))
