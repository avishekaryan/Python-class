print('Calculator')

print('\nPress')
print('1. Add')
print('2. Subtract')
print('3. Multiplication')
print('4. Division')
print('5. Exit')

while True:
    p = int(input('\nEnter the operation : '))

    if p == 1 :
      a = int(input('Enter 1st no. :'))
      b = int(input('Enter 2nd no. :'))
      print('Sum =',a+b)
    elif p == 2:
      a = int(input('Enter 1st no. :'))
      b = int(input('Enter 2nd no. :'))
      print('Subtract =',a-b)
    elif p == 3:
      a = int(input('Enter 1st no. :'))
      b = int(input('Enter 2nd no. :'))
      print(f'Multiplication of {a} and {b} =',a*b)
    elif p == 4:
      a = int(input('Enter 1st no. :'))
      b = int(input('Enter 2nd no. :'))
      print(f'Division of {a}/{b} = ', a/b)
    elif p == 5:
      print('Exiting...')
      break
    else :
      print('Invalid number!')
      print('Enter Displaying no. only')
    
