from itertools import combinations
cl=[]
n=int(input())
l=[i for i in range(n)]
per=[]
for i in range(2,n):
    per.append(list((combinations(l,i))))
print(per)
    
