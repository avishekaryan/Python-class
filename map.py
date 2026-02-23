# WAP to take multiple input in a single line.

x,y,z = map(int,input("Enter 3 values: ").split())

print("The numbers you have entered are : " , x,y,z)

# their sum
print(f"The sum of {x} , {y} and {z} is : " , x+y+z)

# their difference
print("Their difference is : ", x-y-z)

# their product
print("Their product is : " , x*y*z)

# their division 
print("Their division is : " , x/y/z)
 
# their average 
print("Their average is : " , (x+y+z)/3)



