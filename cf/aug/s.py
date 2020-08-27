
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=[]
    l.append(0)
    for i in input().split():
        l.append(int(i))
    if n%k==0:
        print(sum(l))
    else:
        r=n%k
        q=n//k
        if (q+r<n):
            o=(q+k)//k+1
            i=n-q+o
            s=""
            for j in l[(i):]:
                s=s+str(j)
            print(sum(l[:i]),s)
        
    
        
