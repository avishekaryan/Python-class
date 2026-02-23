# List is mutable


List_data = [1,2,3,4,"hello",True]

for item in List_data:
    print(item)

# index searching
print(List_data[4])     # [0,1,2,3,4,5,6,7] 4th position ko value print garcha

# negative indexing
print(List_data[-1])    # last value print garcha 

# list slicing
print(List_data[1 : 4])   # (start : stop : step)

# reverse
print(List_data[ ::-1])


# Python In-built fuction for list

""" 
len()  to return the total length of list
max()  to return the maximum value among list
min()  to return the minimum value from list
sorted()  to start the data with ascending order  (automatically)
sum()     to return the sum of all the list value

 """

list_num = [1,2,3,4,2,4,9,1,0]

print(len(list_num))
print(max(list_num))
print(min(list_num))
print(sorted(list_num))
print(sum(list_num))

a = sorted(list_num)
a.reverse()
print(a)

# list methods

list_num.append(16)
print(list_num)

list_num.insert(5,3)   #insert(index position , value)
print(list_num)


list_num.remove(3)
print(list_num)

list_num.pop(3)
print(list_num)

list_num.sort()
print(list_num)

list_num.extend([12,34,56])
print(list_num)

list_num.clear()
print(list_num)

list_num.append(6)
print(list_num)