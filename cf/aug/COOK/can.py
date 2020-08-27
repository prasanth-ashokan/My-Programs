for _ in range(int(input())):
    n,m,k,l,r=map(int,input().split())
    g=1000000000000007
    for i in range(n):
        t,p=map(int,input().split())
        for j in range(m):
            if t>k+1:
                t=t-1
            elif t<k-1:
                t=t+1
            else:
                t=k
        if t<=r:
            if t>=l:
               if g>p:
                   g=p
    if g==1000000000000007:
            print(-1)
    else:
            print(g)
    
