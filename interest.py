# WAP to calculate simple interst .
# Formula : SI = P*T*R/100

# Taking inputs from user
P = float(input("Enter Principle amount = "))
T = float(input("Enter Time period = "))
R = float(input("Enter Rate = "))

SI = P*T*R/100
print("Simple Interest = P*T*R/100 = " , SI)

# also Compound interest
CI = P*(1+R/100)**T
print("Compound Interest = P*(1+r/100)**T = " , CI)