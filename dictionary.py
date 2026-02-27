# Dictionary      key : value 

# Creating dictionary
data = {"name":"Abhi",
        "roll_no":1,
        "Faculty":"AI"
        }

    #using constructor 

data1 = dict(name = "Abhi",roll_no = 1, faculty = "AI")

print(data)
print(data1)

# Adding item to the Dictionary
data["semester"] = '1st'
print('New data : ',data)

# Updateing item to the Dictionary
data.update({"name":"Abhishek"})
print(data)

# Comparing
dict1 = {"Hi":"Hello","num":2345}
dict2 = {"Greeting":"Namaste"}
x = dict1 == dict2
print(x)

# Methods of Dictionary
"""
get(key) : return particular value from dictionary using key
items()  : to return all the items from dictionary i.e both keys and values
keys()    : to return only keys of dictionary
values()  : to return only values 
update() : to update dictionary key and values 
pop()    : to delete dictionary item from last
"""

# Traversing dictionary

for k in dict1.keys():
    print(k)

for v in dict1.values():
    print(v)

for k,v in dict1.items():
    print(k,v)

for g in dict1.get("Hi"):
    print(g,end="" )

p = dict1.pop("num")
print(dict1)

# Nested dictionary
n = {
    "s1":{"x":10,"y":12},
     "s2":{"a":6,"b":5}
     }
print(n)

# Traversing into nestead dictionary
for k, v in n.items():
    print(k,v)
    for x,y in v.items():
        print(x,y)

