# WAPP to print multiplication table from 1 to 10 using a nested for loop.

for i in range(1,11) :
    print(f'Multiplication table of {i}')
    for j in range(1,11) :
        n = i * j
        print(f'{i} * {j} = {n}')



# Using a function

def multiplication_table():
    for i in range(1,11) :
        print(f'Multiplication table of {i}')
        for j in range(1,11) :
            n = i * j
            print(f'{i} * {j} = {n}')

multiplication_table() 



# print multiplication table upto user input.

num = int(input('Enter a last table number :'))

for i in range(1,num+1) :
    print(f'Multiplication table of {i}')
    for j in range(1,11) :
        n = i * j
        print(f'{i} * {j} = {n}')

'''
We can also use a function to do the same thing.
we just have to pass the user input as argument at last while calling the function.
def multiplication_table(num):
    same conditions and logic
take input from user here out of function in num variable then
multiplication_table(num)
'''

# Write a python program to print multiplication table of a specific number entered by user.
print('\nMultiplication table of a specific number')
num = int(input('Enter a number : '))

print(f'Multiplication table of {num}')
for i in range(1,11) :
    print(f'{num} * {i} = ', num*i)

