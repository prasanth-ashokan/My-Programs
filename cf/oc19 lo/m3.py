for x1 in range(int(input())):
    n,m,q=map(int,input().split())
    r=[]
    c=[]
    for i in range(q):
        x,y=map(int,input().split())
        r.append(x)
        c.append(y)
    sr=0
    sc=0
    e=0
    o=0
    rs=set(r)
    cs=set(c)
    rs=list(rs)
    cs=list(cs)
    f=0
    for i in range(max(len(rs),len(cs))):
        #print(i)
        if q%2==0:
            if i<len(rs):
                a=rs[i]
                if (r.count(a)%2)!=0:
                    sr=sr+n-1
                    f=1
                else:
                    f=0
            print('r',sr,a)
            if i<len(cs):
                a=cs[i]
                if (c.count(a)%2)!=0:
                    sc=sc+m-1
                if f==0:
                    if q!=2:
                        sr=sr+1
                    else:
                        sr=0
            print('c',sc,a)
        else:
            if i<len(rs):
                a=rs[i]
                if (r.count(a)%2)!=0:
                    sr=sr+n-1
                    f=1
                else:
                    f=0
            print('r',sr,a)
            if i<len(cs):
                a=cs[i]
                if (c.count(a)%2)!=0:
                    sc=sc+m-1
                    if f==0:
                        sr=sr+1   
            print('c',sc,a)
    print(sr+sc)
