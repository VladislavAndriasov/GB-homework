with open('test.txt', encoding='utf-8') as text:
    new = text.readlines()

with open('test2.txt', 'w', encoding='utf-8') as text:
    for line in new:
        if '1' in line:
            line = line.replace('One', 'Один')
        elif '2' in line:
            line = line.replace('Two', 'Два')
        elif '3' in line:
            line = line.replace('Three', 'Три')
        elif '4' in line:
            line = line.replace('Four', 'Четыре')
        text.write(line)
