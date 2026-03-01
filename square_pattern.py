# Write a python program to print the square pattern.
'''
* * * * 
* * * *
* * * *
* * * *
'''

n = 4
for i in range(n) :
    for j in range(n) :
        print('*', end=' ')
    print()



# Using a function
def square_pattern(n):
    for i in range(n) :
        for j in range(n) :
            print('*', end=' ')
        print()

square_pattern(4)


# user input 
n = int(input("Enter the number of rows and columns : "))

for i in range (n) :
    for j in range(n) :
        print('*' , end=' ')
    print()


# To print user input square patter 

n = int(input("Enter the number of rows and columns :  "))
pattern = input("Enter the pattern you want to print : ")

for i in range(n) :
    for j in range(n):
        print(pattern, end=' ')
    print()