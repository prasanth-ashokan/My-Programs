from collections import *
for x1 in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split(' ')]
    vis=defaultdict(int)
    w=[0]*(n)
    f=0
    d=defaultdict(int)
    m=l[0]
    g=0
    vis[m]=1
    for i in range(1,n):
        a=l[i]
        m=max(m,a)    
        j=1
        h=l[i]*j
        while(h<=m):
            if vis[h]:
                w[i]=w[i]+vis[h]
                break;
            j=j+1
            h=l[i]*j
        vis[l[i]]+=1
    print(max(w))
            
        
        
