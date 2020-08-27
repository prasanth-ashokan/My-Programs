def eratosthenes(n,l):
    multiples = []
    for i in range(2, n+1):
        if i not in multiples:
            l.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)
    return l
def find(a,l,n,op):
    for j in l:
        f=0
        for i in range(n):
            
            if a[i]%j==0:
                f=1
                a[i]=a[i]//j
        if f==1:
            op=op+1
    c=a.count(1)
    if c==n:
        print(op)
        return True
    else:
        return False
l=eratosthenes(1000000,[])
for x in range(int(input())):
    op=0
    n=int(input())
    a=[int(i) for i in input().split()]
    c=a.count(1)
    
    while(True):
        if find(a,l,n,op):
            break
        
            
            
