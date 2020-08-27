def eratosthenes(l,n):
    multiples = []
    for i in range(2, n+1):
        if i not in multiples:
            l.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)
    return l
l=[]
l.append(1)
n=int(input())
eratosthenes(l,round(pow(n,1/3))
for i in l:
    f=pow(n,3)
    if 
