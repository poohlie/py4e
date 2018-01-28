small = None
large = None
while True:
    sval = input('Please enter a number: ')
    if sval == 'done':
        break
    try:
        fval = int(sval)
    except:
        print('Invalid input')
        continue
    if small == None:
        small = fval
        large = fval
    else:
        if fval < small:
            small = fval
        elif fval > large:
            large = fval
print('Maximum is '+str(large))
print('Minimum is '+str(small))
        