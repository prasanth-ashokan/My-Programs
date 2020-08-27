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
        if r.count(i)%2 !=0 :
            ro+=n-(r.count(i))
            if len(set(c))==len(c):
                ro=ro-len(set(c))
        else:
            if len(set(r))==1 and len(set(c))==1:
                ro=0
            else:
                ro=r.count(i)
    for i in set(c):
        if c.count(i)%2 !=0:
            co+=m-1
    
    print(ro,co,len(set(r)),len(set(c)))  
