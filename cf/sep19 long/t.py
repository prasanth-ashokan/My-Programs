import bisect
b=[2,3,0,9]
def bis(n):
    if n==3 or n==4:
        return 1
    else:
        k=[]
        for ii in range(2,70):
            k.append(pow(2,ii))
        o=bisect.bisect_left(k,n)
        o=o%4
    return (b[o-1])
def brute(n):
    a=[0,1]
    q=[]
    for y in range(2,n-1):
            t=a[y-2]
            r=a[y-1]
            a.append((t+r))
            r=a
    while(len(a)>=2):
            l=a
            a=[]
            for iii in range(1,len(l),2):
                a.append(l[iii])
    return (a[0]%10)
for i in range(100,200):
    if brute(i)!=bis(i):
        print(i)
print("over")
       
    




