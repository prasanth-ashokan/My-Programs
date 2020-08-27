def pro(n):
    if(n==0):
        return(1)
    else:
        f=1
        for i in range(1,n+1):
            f=f*i
    return(f)
        
t=int(input())
while(t!=0):
    n,k=map(int,input().split())
    l1=list(map(int,input().split()))
    l1.sort()
    l2=l1[0:k:1]
    c1=l2.count(l2[-1])
    c2=l1.count(l2[-1])
    n1=pro(c2)
    r=pro(c1)
    r1=pro(c2-c1)
    y=r*r1
    x=n1/y
    print(int(x))
    t=t-1
