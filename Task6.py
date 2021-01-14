day_result = int(input('First day result: '))
goal = int(input('Enter goal: '))
days = 1
print('Результат:')
print('1-й день: 2')
while day_result < goal:
    day_result = day_result * 1.1
    days += 1
    print(f'{days}-й день: {day_result:.2f}')
print('На ',days,'-й день спорстмен достиг результата - не менее ', goal, ' км.')