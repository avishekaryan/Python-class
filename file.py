# file opening and creating using exclusive mode
"""
fp = open("try.txt" , "x")
print("File created sucessfully")
fp.close()
"""

# file opening , creating and writing using w/writing mode 

# new = open("temp.txt" , "w")
# print("File created sucessfully")
# new.close()


# new = open("temp.txt" , "w")
# new.write("Learning to create and write on a created file.")
# print("Write sucessfully")
# new.close()

# Reading the file just created from w mode

# new = open("temp.txt" , "r")
# reading = new.read()
# print(reading)
# new.close()

# new = open("temp.txt" , "w")
# new.write("Learning to override.")
# print("Write sucessfully")
# new.close()


# Append

# new = open("temp.txt" , "a")
# new.write("\n Appending new data and information.")
# print("Append sucessfully")
# new.close()


# Using with statement 

# with open("demo.txt" , "w") as fp:
#     fp.write("Writing data using with statement")
#     print("Write sucessfully")


# with open("demo.txt" , "a") as fp:
#     fp.write("\n Appending new data using with statement.")
#     print("Append sucessfully")


# Read using with

# with open("demo.txt" , "r") as fp:
#     reading = fp.read()
#     print(reading)


# Using try catch exception handeling

# try:
#     avhi = open("here.txt" , "r")
#     avhi.close()
# except FileNotFoundError:
#     print("Oops File not found!")
# finally:
#     print('exit')
  

# try:
#     avhi = open("demo.txt" , "r")
#     reading = avhi.read()
#     print(reading)
#     avhi.close()
# except FileNotFoundError:
#     print("Oops File not found!")


# Reading and writing in the same file


# new = open("temp.txt" , "w+")
# new.write("Learning to create and write on a created file.")
# print("Write sucessfully")
# new.seek(0)
# reading = new.read()
# print(reading)
# new.close()

  
# new = open("temp.txt" , "a+")
# reading = new.read()
# print(reading)
# new.seek(0)
# new.write("\nLearning to create and write on a created file. Tried 2nd time.")
# print("Write sucessfully")
# new.close()


# Creating  and writing into binary file

# avhi = open("binary.bat" , "wb")
# m = b'Hello python!'
# avhi.write(m)
# print("Write sucessfully")
# avhi.close()



# Creating file in absolute File
# fp = open("C:\\test\\man.txt", 'w')
# print("File created sucessfully")
# fp.close()


# fp = open("C:\\test\\man.txt", 'w')
# msg = ("Hello, Trying to write using absolute path.")
# fp.write(msg)
# print("Wite sucessfully")
# fp.close()


# Write a number to a file

# fp = open("try.txt" , "w")
# for i in range(1,6):
#     fp.write(str(i))
# print("Write Sucessfully")
# fp.close()


# Reading number from a file

# fp = open("try.txt" , "r")
# for i in fp:
#     reading = int(i)
#     print(reading)
# fp.close()


# Reading image from a file 

# fp = open("img.jpg", 'rb')
# image = fp.read()
# print(image)
# fp.close()



# Question 

fp = open("try.txt", "r+")
list = ['Hello' , '\n Python', '\n Nepal', '\n Nice to meet you.']
fp.writelines(list)
print("Written in file sucessfully.")
fp.seek(0)
reading = fp.readlines()
print(reading)
fp.close

