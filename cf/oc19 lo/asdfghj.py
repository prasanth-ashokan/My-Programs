for x1 in range(int(input())):
    n,m,q=map(int,input().split())
    r=[]
    c=[]
    for i in range(q):
        x,y=map(int,input().split())
        r.append(x)
        c.append(y)
    o=0
    for i in set(r):
        for j in set(c):
            if r.count(i)%2!=0:
                if c.count(i)%2!=0:
                    o=n+m-2
                else:
                    pass
            else:
                if c.count(i)%2==0:
                    o=0
                else:
                    pass
        
    print(o)
"""if r.count(i)%2!=0:
                if c.count(i)%2!=0:
                    o+=(n-1)+(m-1)
                else:
                    o+=(m-1)
            else:
                if r.count(i)%2!=0:
                    o+=(n-1)+(m-1)
                else:
                    o+=(m-1)
            print(o)"""
