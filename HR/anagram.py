for _ in range(int(input())):
    a,b=input(),input()
    l=[(i) for i in a]
    p=[i for i in b]
    l=sorted(l)
    p=sorted(p)
    d=sorted(p)
    print(l,p,d)
    q=len(l)
    w=len(p)
    c=0
    for i in l:
        if i in d:
            c=c+1
            d.remove(i)
    print(q+w-(2*c))
