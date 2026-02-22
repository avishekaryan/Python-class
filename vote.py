# WAP to find if a person is eligiable to vote or not.

age = int(input("Enter your age: "))
if age >= 18 :
    print("You are eligible to vote")
else:
    print("Not eligible to vote")


# WAP to find if a person is eligiable to vote or not in Nepal.

age = int(input("Enter your age: "))
if age >= 18 :
    citizen = input("Enter the country name : ")
    if citizen == "Nepal" or citizen =="nepal" :
        print("You are Eligible to vote.")
    else :
        print("You are not Nepali.")
else :
     print("You are not Eligible to vote.")
