# Question
"""
Take a input from user
string(name)
int(roll no)
expression(marks) - eval()
and print total marks in float value 

"""


# Answer

name=input("Enter your name: ")
Roll_no=int(input("Enter your roll no: "))
faculy = input("Enter your faculty : ")
marks=input("Enter your obtained marks of each subject: ")  # eg. 80+90+85
Total_marks=eval(marks)
print("Total_marks : ",Total_marks)