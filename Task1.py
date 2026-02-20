"""Question
 1) comment
 2) double line comment
 3) write a program to calculate the sum of 2 numbers taking input from users
 4) convert the integer value into float value in same program
 5) check the type of each variable data type """


# w.a.p to sum 2 numbers taking input from users
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
add = a + b
print(add)

# convert integer value into float value
a_float = float(a)
b_float = float(b)
sum = a_float + b_float
print("the value in flot",sum)
print(type(sum))
print(type(a_float))
print(type(b_float))