# Question 1

# W.A.P. to find the greatest of 2 numbers by taking input from user .
num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")
print(f"Greatest number from {num1} and {num2} is: ", max(num1, num2))

# using if/else
num3 = int(input("Enter 1st number: "))
num4 = int(input("Enter 2nd number: "))
if num3>num4 :
    print(f"{num3} is the Greatest number than {num4}")
elif num3 == num4 :
    print(f"{num3} and {num4} are Equal")
else :
    print(f"{num4} is the Greatest number than {num3}")    
 