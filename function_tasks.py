# chapter 5 assignments 

'''
parameter = placeholder / variable inside function definition 
argument  = actual value / value given to function
'''


# 1. Write a python program to create a function that takes two numbers as parameters and returns their sum.

def sum(a,b):
    return a+b 

a = int(input('Enter your 1st number: '))
b = int(input('Enter your 2nd number: '))
result = sum(a,b)
print(f"The sum of {a} and {b} is " , result)


# 2. W.A.P.P to create function that accepts a number as argument and checks whether it is prime or not. 

def check_prime(num):
     if num > 1 :
         for i in range( 2,num):
            if num % i == 0 :
                print(f'{num} is NOT a Prime number.')
                break
         else :
             print(f'{num} is a Prime number.')
    
num = int(input('Enter number to verify Prime : '))
check_prime(num)


# 3. W.A.P.P to create function using assert statement to check that the input number is positive.If not , the program should give an error.

def check_positive(num):
    assert num > 0 , "Error : Number must be Positive!"
    print(f'Tne number you entered {num} is positive')

num = int(input("Enter a number: "))
check_positive(num)



# 4. W.A.P.P to create a function that accepts a string and returns the number of vowels in it.

def vowels_count(letter):
    count = 0
    vowels = 'aeiouAEIOU'
    for ch in letter:
        if ch in vowels :
            count += 1 
    return count

letter = input("Enter letters/word : ")
result = vowels_count(letter)
print("Number of Vowels : ",result)



# 5. W.A.P.P to demonstrate the use of : Local variable and Global variable.

# Global variable declared outside the function
n = 10

def function():
    # Local variable declared inside the function
    n1 = 28
    sum = n + n1 
    print(f'Global variable: ',n)
    print(f'Local variable : ',n1)
    print("Their sum = ", sum)

function()
'''
Here 
print(n) will give 10 as output because global variable can be called in this entire program.
print(n1) will give an error showing not declared because local variable can only be used inside the function.
'''



# 6. W.A.P.P for recursive function to calculate the factorial of a given number.

def factorial(num):
    if num == 0 or num == 1:
        return 1
    elif num < 0 :
        print('Fcatorial does not exist for Negative Numbers')
    else :
        return num * factorial(num-1) 
    
num = int(input("Enter any number: "))
result = factorial(num)
print(f'Factorial of {num} = ',result)




# 7. W.A.P.P for recursive function to generate the Fibonacci number at position n.

def fibo(num):               # In short i have written fibonacci as fibo
    if num == 0 :
        return 0 
    elif num == 1 :
        return 1 
    else :
        return fibo(num - 1) + fibo(num - 2)
    
num = int(input("Enter any position : "))
result = fibo(num)
print(f"Fibonacci of {num}th position = ",result)




# 8. W.A.P.P for recursive function to find the sum of digits of given number.

def recursive_sum(num):
    if num == 0 :
        return 0
    else:
        rem = num % 10 
        sum = rem + recursive_sum(num//10)
        return sum
    
num = int(input("Enter any number of 2 or more digits: "))
result = recursive_sum(num)
print(f'The sum of {num} digits is ',result)



# 9. W.A.P.P for a recursive function to find the sum of first n natural numbers.
'''
     Example:
     Input : 1234 (n=4 then 1 + 2 + 3 + 4)
     Output : 10
'''

def recursive_sum(num) :
    if num == 1:
        return 1
    else :
        return num + recursive_sum(num-1)
    
num = int(input("Enter positive number : "))
result = recursive_sum(num)
print(f'The sum of first {num} natural numbers = ',result)



# 10. W.A.P.P for a function to calculate the area of a circle. Take radius as parameter.

pi = 3.14
def area(radius):
    area = pi * radius * radius
    return area 

radius = float(input("Enter the Radius of circle: "))
result = area(radius)
print("The Area of Circle = ",result)



# 11. W.A.P.P for a function that takes three numbers and returns the smallest among them.

def smallest(a,b,c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c :
        return b
    else :
        return c
    
a = float(input("Enter 1st number : "))
b = float(input("Enter 2nd number : "))
c = float(input("Enter 3rd number : "))
result = smallest(a,b,c)
print(f'Smallest number among {a} , {b} and {c} is ' , result)




# 12. W.A.P.P that accepts a number and print its multiplication table.

def table(num):
    for i in range(1,11):
        print(f'{num} * {i} = ',num*i)

num = int(input("Enter a number: "))
print("The Multiplication table of ",num) 
table(num)




# 13. W.A.P.P for a recursive function to find the LCM of two numbers.

''' GCD = Greatest common divisor   and  HCF = Highest common factor  , both are same '''
def gcd(x,y):
    if y == 0 :
        return x
    else :
        return gcd(y, x % y)
    
def lcm(x,y):
    return (x * y)// gcd(x,y)
    
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
result = lcm(x,y)
print(f'LCM of {x} and {y} is ',result)

      # Another way

def lcm(a,b,i=1):
    if i % a == 0 and i % b == 0 :
        return i
    return lcm(a,b,i+1)

a,b = map(int,input("Enter 2 numbers: ").split())
result = lcm(a,b)
print(f"The LCM of {a} and {b} is " , result)
