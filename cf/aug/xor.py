def xor(x):
    x1=x[0]
    for i in range(1,len(x)):
        x1^=x[i]
    return x1
from collections import *
for _ in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split()]
    c=0
    d=defaultdict(lambda:False)
    for i in range(0,n):
        for j in range(i,n):
            for k in range(j,n):
                x,y=l[i:j],l[j:k+1]
                if len(x)>0 and len(y)>0:
                    print(i+1,j+1,k+1)
    print(c)
                    
                    
            
