# Write a Python program to print a pattern using nested loops:
'''
*
**
***
****
*****
'''
# This pattern is called Right-angled triangle pattern / Half pyramid pattern / Increasing triangle pattern.

n = 5                          # no of rows 
for i in range(1,n+1): 
    for j in range(i):         # inner loop to print stars in each row       
        print('*', end=' ')
    print()


# WAPP to print a following pattern using nested loops :
'''   
*****
****
***
**
*
'''
# This pattern is called Inverted Right-angled triangle pattern / Inverted Half pyramidstar pattern / Decreasing triangle pattern.

print('\nThis is Reverse/inverted pattern')
for i in range(n,0,-1) :           # n is global variable 
    for j in range(i) :
        print('*',end=' ')
    print()

    # another method/way

for i in range(0,n+1) :
    for j in range(n-i) :          # instead start i in range from 1 then j in range from n+1-i
        print('*' , end=' ')
    print()


# Write a Python program to print a follwing pattern using nested loops:
1
22
333
4444
55555

n = 5 
for i in range(1,n+1) :
    for j in range(i) :
        print(i , end=' ')
    print()


#  Write a Python program to print star pyramid pattern:
''' 
    *
   ***
  *****
 *******
********* 
'''
# This pattern is also called Centered paramid pattern / Full pyramid pattern.

n = 5 
for i in range(1,n+1) :
    for j in range(n-i) :
        print(end='  ')           # double space bar inside end
    for k in range(2*i-1) :
        print('*', end=' ')
    print()


# Write a python program to print following pattern 
'''
     1
    222
   33333
  4444444
 555555555
'''
n = 5
for i in range(0,n+1) :
    for j in range(n-i) :
        print(end='  ')
    for k in range(2*i-1) :
        print(i ,end=' ')
    print()


# WAPP to print the following pattern 
'''
            *
           **
          ***
         ****
        *****
'''
# This pattern is called a Right-Aligned Triangle Pattern / Right-Justified Star Pattern .

n = 5 
for i in range(1,n+1) :
    for j in range(n+1-i) :
        print(end='  ')
    for k in range(i) :
        print('*' , end=' ')
    print()


#  WAPP to print the follwing pattern 
'''
      *****
       ****
        ***
         **
          *
'''
# This pattern is called Inverted Right-Aligned Triangle Pattern / Inverted Right-Justified Star Pattern.

n = 5
for i in range(1,n+1) :
    for j in range(i) :
        print(end='  ')
    for k in range(n+1-i) :
        print('*' , end=' ')
    print()

