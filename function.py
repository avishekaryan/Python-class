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