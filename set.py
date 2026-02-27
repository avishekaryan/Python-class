# Set

# set operations
"""
union(|) : All the values from both sets are returned
intersection(&) : common value from both sets are return
difference(-) : value that is present in set A but not in B
symmetric difference (^) : value that are not common in either of sets 
"""

# Program

set1 = {1,2,3,4,5}              # defined using curley bracket {}
set2 = set((6,7,8,4,2))         # defined using set constructor, set(())

u = set1|set2
print('Union = ',u)

i = set1 & set2
print('Intersection = ', i)

d = set1 - set2
print('Difference of set1 - set2= ',d)

s = set1^set2
print('Symmetric difference = ',s)

# add()
set1.add(15)
print(set1)

# update()
set1.update(set2)
print(set1)