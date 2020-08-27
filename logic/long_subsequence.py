t=int(input())
for x in range(t):
    n=int(input())
    l=[int(i) for i in input().split()]
    w=[]
    wl=[]
    for i in range(n):
        a=l[i]
        p=[a]
        for j in range(i+1,n):
            b=l[j]
            if(a<b):
                a=b
                p.append(b)
        w.append(p)
        wl.append(len(p))
    w=sorted(w)
    m=max(wl)
    print(w)
for i in w:
    if(len(i)==m):
        print(i)
            
        
        
