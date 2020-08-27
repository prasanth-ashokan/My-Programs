for x1 in range(int(input())):
    n,m,q=map(int,input().split())
    r=[]
    c=[]
    for i in range(q):
        x,y=map(int,input().split())
        r.append(x)
        c.append(y)
    ro,co=0,0
    for i in set(r):
        if r.count(i)%2 !=0:
            ro+=(n)
            if c.count(i)%2==0:
                ro=ro-len(set((c)))
            else:
                ro=(ro-c.count(i))
        else:
            ro=len(set(c))
    for i in set(c):
        if c.count(i)%2 !=0:
            co+=(m)
            if r.count(i)%2==0:
                co=co-len(set((r)))
            else:
                co=(co-r.count(i))
        else:
            co=len(set((r)))

    print(ro,co,len(set(r)),len(set(c)))  
