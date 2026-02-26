# WAP to demonstrate operator precedence using arithematic operators.

# iniatializing the variables
a = 10 
b = 4 
c = 12
d = 7

# If question is 
a + b * c - d 
"""
 then multiplication will be performed first then addition and then substraction
 because multiplication (*) has higher precedence . Both + and - have same precedence
 so we consider associativity at that time.
"""

# Examples
print("a,b,c,d = " , a,b,c,d)

print("a+b*c = ",a+b*c)        

print("(a+b)*c =", (a+b)*c)

print("a-b/d =", a-b/d)

print("a/(c-d)+b =", a/(c-d)+b)

""" 
As we know that 
1. Parentheses have the highest precedence, so expressions inside parentheses are evaluated first.
2. Exponentiation (**) is evaluated next, followed by multiplication (*), division (/), and modulus (%).
3. Addition (+) and subtraction (-) are evaluated last, and they have the same precedence, so they are evaluated 
   from left to right (associativity).
"""