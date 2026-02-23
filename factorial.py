# WAP to find factorial of a number using recursion

def recursive_factorial(n) :
    if n == 1 :
        return n
    else :
        return n * recursive_factorial(n-1)

total = recursive_factorial(5)
print(total)



# Taking input from user

n = int(input("Enter any number: "))
fact = recursive_factorial(n)
print(fact)

