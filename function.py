# Using lambda function

addition = lambda a,b : a+b
print(addition(4,2))

square = lambda a: a*a
print(square(6)) 


# Question from function

def f(x=[]):               # jati palta function call huncha tayti vale add hudaie jancha
    x.append(1)             
    print(x)
f()
f()


# function by passing argument

def addition(a,b) :
    sum = a + b 
    print(f"The sum of {a} and {b} is {sum}")

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number: "))
addition(a,b)


# another way to pass argument

def sum(c,d):
    return c+d

c = int(input("Enter 1st number: "))
d = int(input("Enter 2nd number: "))
result = sum(c,d)
print(f"The sum of {c} and {d} is ", result)