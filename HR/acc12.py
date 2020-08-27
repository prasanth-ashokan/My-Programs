from math import ceil as c
n,q=map(int,input().split())
l=[int(i) for i in input().split()]
for i in range(q):
    a,b=map(int,input().split())
    t=(b*(b+1))/2
    a=a-1
    r=(a*(a+1))/2
    #print(t,a)
    t=t-r
    o=b-a
    #print(o)
    print(c(t//o))
    
