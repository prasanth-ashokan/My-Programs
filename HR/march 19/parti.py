n,l,r=map(int,input().split())
a=[int(i) for i in input().split()]
c=0
b=[]
from itertools import permutations  
perm = permutations(a,2) 
for i in list(perm):
    k=sum(i)%1000000007
    if k in range(l,r) and k not in b:
        c=c+1
        print(i)
        b.append(k)
print(c)
