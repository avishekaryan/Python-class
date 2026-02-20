# Question
"""Take a input from user
string(name)
int(roll no)
expression(marks) - eval()
and print total marks in float value """

# Answer

name=input("Enter your name: ")
Roll_no=int(input("Enter your roll no: "))
marks=input("Enter your obtained marks of each subject: ")
Total_marks=eval(marks)
print("Total_marks : ",Total_marks)