
# Different methods of list using loop and nested if.

"""
# WAP to check items in or not in a list using loop.

list = [6,9,2,7,8,4]

n = int(input("Enter a number:"))
for i in list:
    if i == n:
        print(" is found")
        break
else:
    print(" is not found")

# similarly
for i in list:
    if i not in list:
        print(f'{i} not found')
        break
else:
    print(f'{i} is found')
"""

"""

# WAP to insert 5 list values using for loop.
list = []
for i in range(5):
    n = int(input("Enter a number: "))
    list.append(n)

print(list)


# Dynamically taking length of list 

list1 = []
a = int(input("Enter range:"))
for i in range(a):
    num = int(input("Enter a number: "))
    list1.append(num)

print(list1)



# WAP to join 2 list using loop

list2 = [1,2,3,4,5]
list3 = [8,7,6,5,4]
for newlist in list2:
    print(newlist)
    list3.append(newlist)
print(list3)



# filter the duplicate items using loop

list = [1,2,3,4,5]
list2 = [1,3,5,7,9]
list3 = list + list2
filtered_list = []

for item in list3:
    if item not in filtered_list:
        filtered_list.append(item)

print(filtered_list)
    

# Search the specific items infrom list using user input 

list = [2,3,5,7,11,13]
search = int(input("Enter the value to Search :"))

for item in list:
    if item == search :
        print(f"{item} is found")
        break 
else:
    print(f'{search} is not found')



# Nestead list(2D list)

list = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

for nestead_list in list :
    print(nestead_list)

for list1 in list:
    for data in list1:
        print(data)

# for searching item
search = int(input("Enter search value: "))
for data in list:
     if search in data:
          print(f'{search} is found')
          break
else :
     print(f'{search} not found')

# Another process 
for list1 in list:
     for data in list1:
          if search == data:
               print(f'{data} found')
               break
          
"""
# Update value of the list 
list = [1,2,3,4,5]
list[1] = 0
print(list)