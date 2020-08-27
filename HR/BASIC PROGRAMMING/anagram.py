for  _ in range(int(input())):
    c,s=0,0
    a=[i.split() for i in input()]
    b=[i.split() for i in input()]
    sorted(a)
    sorted(b)
    m=max(a,b)
    n=min(a,b)
    l=len(a)+len(b)
    for i in m:
        if i in n:
            s+=m.count(i)-n.count(i)
            c=c+1
    print(l-(2*c))
