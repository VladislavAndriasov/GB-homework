y = 0
while True:
    x = (input('enter numbers (enter S to stop): ')).split()
    z = 0
    while len(x) > 0:
        try:
            z = int(x.pop(0))
            y = y + z
        except ValueError:
            print('Stopped')
            break
    print('Result: ', y)


