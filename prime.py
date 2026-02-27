# WAP to check whether a number is prime or not using a loop.

num = int(input("Enter a number: "))

if num <= 1 :
    print(f'{num} is not a Prime number.')
else:
    for i in range( 2,num):
        if num % i == 0 :
            print(f'{num} is not a Prime number.')
            break
    else :
            print(f'{num} is a Prime number.')
        
'''
In this for loop , 
we are checking if the number is divisible by any number from 2 to num-1.
1.If it is divisible by any of those numbers, then it is not a prime number 
    because it has a divisor other than 1 and itself as 1 and num are not in 
    the range of 2 to num-1.
    so if remainder comes 0 inside the loop, it means that num is divisible by i 
    and hence it is not a prime number.
 
 NOTE : Prime numbers are defined as natural numbers greater than 1 that have 
        no positive divisors other than 1 and themselves.
        so its divisors count must be exactly 2 (1 and itself). 
 
    In that case, we print that it is not a prime number and
    we break out of the loop.Then else part is not executed.

2.If the loop completes without finding any divisors, then the number is a prime number and
  we print that it is a prime number.

'''

# Similarly another process to check weather a number is prime or not using divisor counting.

n = int(input("Enter a number : "))

if n <= 1:
    print(f"{n} is not a Prime number.")
else:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    
    if count == 2:
        print(f"{n} is a Prime number.")
    else:
        print(f"{n} is not a Prime number.")