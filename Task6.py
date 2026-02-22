# Question

""" Take a input from user
Enter name of students
Enter marks of 6 subjects
Pass mark : 32
Total marks per subject : 100
Overall pass mark : 240
Total marks in all subject : 600
Calculate total obtained marks in all subject
Display result pass/fail 
Find percentage and display the grade. """


# Solution
name = input("Enter the name of student: ")
a = float(input("Enter marks obtained in AI : "))
p = float(input("Enter marks obtained in Python: "))
s = float(input("Enter marks obtained in Sociology: "))
c = float(input("Enter marks obtained in Calculus: "))
e = float(input("Enter marks obtained in English: "))
d = float(input("Enter marks obtained in Digital logic: "))

total_obtained = a + p + s + c + e + d
print(f"Total marks of {name} is: ", total_obtained)

if a>=32 and p>=32 and s>=32 and c>=32 and e>=32 and d>=32 and total_obtained>=240 :
    print("**Pass**")
else :
    print("**Fail**")

percentage = ( total_obtained / 600 )* 100
print("Percentage = " , percentage ,"%")

if percentage > 90 :
    print("Grade : **A+**")
elif percentage >80 :
    print("Grade : **A**")
elif percentage >70 :
    print("Grade : **B+**")
elif percentage >60 :
    print("Grade : **B**")
elif percentage >50 :
    print("Grade : **C+**")
elif percentage >40 :
    print("Grade : **C**")
elif percentage >35 :
    print("Grade : **D**")
else :
    print("Grade : **NG**")


