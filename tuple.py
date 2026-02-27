# Tuple 
# processes to create/make/construct tuple 

"""
x = 1,2,3,4
print(x)
print(type(x))

tup = (1,2,3,4)
print(tup)

t = tuple((6,7,8,9,0))
print(t)

# Type conversion  tuple into list then agian list into tuple
l = list(tup)
l.append(7)
y = tuple(l)
print(y)

tuple=(1)
print(type(tuple))

tuple=(2,)
print(type(tuple))

"""

# In-built functions of tuple

# Sort : Arrange data of tuples in ascending order
t = (1,5,6,0,3)
s = sorted(t)
print(s)

# indexing    index position value
i = t[3]
print(i)

# negative indexing
print(t[-4])

# slicing 
print(t[1:4])

# negative slicing
print(t[-3:-1])

# Traverse tuple from list
z = [(1,2,3),(4,5,6),(2,4,8)]
for a,b,c in z:
    print(f'first value is {a} , second value is {b} & third value is {c}')


# nestead tuple
T = (1,2,(3,4),(5,6,7))
for data in T :
    print(data)

# Packing
Tuple = 1,3,5,7,9
print(Tuple)

# Unpacking
a,b,c,d,e = Tuple
print(a,b,c,d,e)

# Ziping
print(zip(Tuple))

tup1 = ('abhi','nepal','hello')
tup2 = ('name','country','greet')
p = zip(tup1,tup2)
q = list(p)

print(p)
print(q)

# Unzipping 
u,v = zip(*q)
print(u)
print(v)