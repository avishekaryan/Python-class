# Second class 

# On Relative path

# Creating file
file = open("demo.txt","x")
if file:
    print("File created sucessfully.")
else:
    print("File already exist.")

# Creating file using with
with open("demo1.txt","x") as file:
    print("File created sucessfully.")


# Creating file using exceptional handeling

try :
    file = open("try3.txt","x")
    print("File created sucessfully")
    file.close()
except FileNotFoundError: 
    print("File doesn't exist !")

# another way using with
try:
    with open("create.txt","x") as file:
        print("File created successfully using with statement")
except FileNotFoundError :
    print("File doesn't exit!")



# To write into the file

file = open("demo.txt","w")
message = ("Hello Python world ")
writing = file.write(message)
print("Writing sucessfully")
file.close()

# Writing again on the same file
file = open("demo.txt","w")
msg = "\n Existing data modified/overwrite"
writing = file.write(msg)
print("Overwrite into file sucess")
file.close()


# To append new data into the file 

with open("demo.txt","a") as fp:
    msg = ("\n We are learning file handeling")
    writing = fp.write(msg)
    print("Append into file Sucess")




# Using exceptional handeling to write

try :
    with open("demo1.txt","w") as fp:
        msg = "We are Learning File handeling"
        fp.write(msg)
        print("Sucess")

except FileNotFoundError:
    print("File doesn't exist")

finally:
    print("Exit")    



# To Read from the file

fp = open("demo.txt","r")
reading = fp.read()
print(reading)
fp.close()


# Reading from file using Exceptional file handeling

try :
    with open("demo.txt","r") as fp:
        reading = fp.read()
        print(reading)
except FileNotFoundError:
    print("Oops! File not fount")
finally :
    print("Exit")



# Trying to Read and write on same file using r
try :
    with open("demo.txt","r") as fp:
        reading = fp.read()
        print(reading)
        writing = fp.write("How are you?")
except FileNotFoundError:
    print("Oops! File not fount")
finally :
    print("Exit")
# It gives an error.


# Writing and Reading on same File 
#     Using r+ and w+ overwite the existing data and read

fp = open("demo1.txt","w+")
msg = "Hello file."
fp.write(msg)
print("Write sucess")
fp.seek(0)
reading = fp.read()
print(reading)
fp.close()


# Using with Writing and Reading on same file

with open("demo1.txt","r+") as fp:
    msg = "Hello Changing existing data."
    fp.write(msg)
    print("Write sucess")
    fp.seek(0)
    reading = fp.read()
    print(reading)



# Reading and writing on same file it doesn't need seek function as read works 1st

fp = open("demo.txt","r+")
reading = fp.read()
print(reading)
msg = "\n Everthing will work."
fp.write(msg)
print("Write sucess")
fp.close()



# Creating,Opening ,Writing and Reading in binary file

file = open("demo.bat","wb")
print("Create sucess")
file.close()

# writing
file = open("demo.bat","wb")
msg = b"I am here today to practise"
file.write(msg)
print("Write sucess")

# Reading
file = open("demo.bat","rb")
reading = file.read()
print(reading)

# Reading image 
file = open("IMG_2025_11_23_161153431.jpg","rb")
reading = file.read()
print(reading)

# Writing number into file 

file = open("demo.txt","w")
msg = 1,2,3,4,5
file.write(str(msg))
print("Write sucess")



# Reading number from file

file = open("demo.txt","r")
reading = eval(file.read())
print(reading)
file.close()
print(type(reading))