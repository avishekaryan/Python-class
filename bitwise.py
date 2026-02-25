# WAP to perform bitwise AND and OR on two numbers and print its binary value. 

a = 5
b = 7

print(f"Binary value of {a} is :", bin(a))
print(f"Binary value of {b} is :", bin(b))

# Operations 
AND = a & b      # output will be 1 when both input is 1 otherwise output will be 0
OR = a | b       # output will be 1 when any one input is 1 otherwise output will be 0

print(f"Bitwise AND of {a} and {b} is : " , AND)
print(bin(AND))

print(f"Bitwise OR of {a} and {b} is : ", OR)
print(bin(OR))

