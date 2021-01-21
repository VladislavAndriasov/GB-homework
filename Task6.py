products = []
position = 0
item_list = []
value_list = []
quantity_list = []
measure_list = []
while input('Do you like to add items?(yes or no)') == 'yes':
    position += 1
    my_dict = {'Name': 1, 'Value': 2, 'Quantity': 3, 'Measure': 4,}
    item = input('Enter item name: ')
    value = input('Enter item value')
    quantity = input('Enter item quantity')
    measure = input('Enter item measure')
    my_dict['Name'] = item
    my_dict['Value'] = value
    my_dict['Quantity'] = quantity
    my_dict['Measure'] = measure
    item_list.append(item)
    value_list.append(value)
    quantity_list.append(quantity)
    measure_list.append(measure)
    products.append(tuple([position, my_dict]))
    analytics = {"Name": item_list, "Value": value_list, "Quantity": quantity_list, "Price": measure_list}
print("Товары: ", products)
print("Аналитика: ", analytics)
