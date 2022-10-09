 # creating an empty set
b = set()
print(type(b))
 
 # adding values to an empty set

b.add(4)
b.add(4)# adding the same value repeatedly does not changes a set 
b.add(6)
b.add(41)
b.add(1)
b.add(4)
b.add((4,56,2))# we can add the  tuples in sets 
#b.add({4:5})# cannot add list or dictionary to sets

print(b)
# length of the set 
print(len(b))
#removal of item 
b.remove(41) # removes 5 from set b
print(b)
#b.remove(23)
print(b.pop())# it removes any elements from the set
print(b)
print(b.clear())# it clear the set
print(b)