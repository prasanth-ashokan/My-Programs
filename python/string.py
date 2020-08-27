# A Python program to print all 
# permutations of given length 
from itertools import permutations,combinations

# Get all permutations of length 2 
# and length 2
c=0
for j in range(1):
    perm = combinations(['a','b','c','e','d'], 2) 

    # Print the obtained permutations 
    for i in list(perm):
            c=c+1
            print(i)
print(c)
c=0
l=[]
perm = permutations(['a','b','c','d','e'],3 ) 

    # Print the obtained permutations 
for i in list(perm):
            c=c+1
            print(i)
print(c)
