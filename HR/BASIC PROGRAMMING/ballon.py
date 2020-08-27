for _ in range(int(input())):
    a,b=map(int,input().split())
    d,c=0,0
    for __ in range(int(input())):
        r,t=map(int,input().split())
        if r==1:
            c=c+1
        if t==1:
            d=d+1
    q=max(a,b)
    w=min(a,b)
    e=max(c,d)
    r=min(c,d)
    print((w*e)+(q*r))
    
