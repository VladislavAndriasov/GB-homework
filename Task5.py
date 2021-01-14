proceeds = int(input('Enter proceeds value: '))
costs = int(input('Enter costs value: '))
if proceeds > costs:
    print('Выручка больше издержек')
    profit = proceeds / costs
    print('Рентабельность выручки: ', profit)
elif costs > proceeds:
    print('Издержки больше выручки')
else:
    print('Выручка равна издержкам')
staff = int(input('Enter the number of employees: '))
profit_per_person = (proceeds - costs) / staff
print(f'Прибыль фирмы на сотрудника равна: {profit_per_person:.2f}')