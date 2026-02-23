# WAP to find the greatest of 3 numbers using if/else condition and taking input from users.
# it will be valid only for 3 different numbers


n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))

if n1 > n2 and n1 > n3 :
    print(f"{n1} is the Greatest number.")
elif n2 > n1 and n2 > n3 :
    print(f"{n2} is the Greatest number.")
else :
    print(f"{n3} is the Greatest number.")


# Using nested if
if n1 > n2 :
    if n1 > n3:
        print(f"{n1} is the Greatest number")
    else :
        print(f"{n3} is the Greatest number")
elif n2 > n3 :
    if n2 > n1 :
        print(f"{n2} is the Greatest number")
    else:
        print(f"{n1} is the Greatest number")
else :
    print(f"{n3} is the Greatest number")