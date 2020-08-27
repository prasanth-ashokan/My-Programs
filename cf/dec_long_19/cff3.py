def qwe(l,ld,ap,n):
    f=0
    for i in (l):
        if(l.count(i)>1) and i!=-1:
            y=0
            for j in range(l.count(i)-1):
                fi=l.index(i)
                l[fi]=-1
                ni=l.index(i,fi+1)
                y=ni+1
                dbi=ni-fi
                if dbi==1:
                    return n-1
                    break;
                
                ld.append(dbi)
                ap.append(i)
                f=1
    if f==0:
        return (0)
    else:
        return (len(l)-(min(ld)))
for _ in range(int(input())):
    l=[]
    ld=[]
    ap=[]
    d={}
    n=int(input())
    a=input()
    
    for i in a:
        l.append(i)
    print(qwe(l,ld,ap,n))
