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
    dd=defaultdict(list)
    l5=[]
    for i in range(0,n):
        for j in range(i,n):
            for k in range(j,n):
                x,y=l[i:j],l[j:k+1]
                if len(x)>0 and len(y)>0:
                    fn1=str(i)+'#'+str(j-1)
                    fn2=str(j)+'#'+str(k)
                    if not d[fn1]:
                        d[fn1]=xor(x)
                        dd[d[fn1]].append(fn1)
                    if not d[fn2]:
                        d[fn2]=xor(y)
                        dd[d[fn2]].append(fn2)
    for i in sorted(dd.keys()):
        print(i,dd[i])
                    
            
