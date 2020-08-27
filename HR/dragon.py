n,k=map(int,input().split())
l=[int(i) for i in input().split()]
c=0
for i in l:
    for j in range(n):
        if  l[j]%i==0 or i%l[j]==0:
            if (i*l[j])%k!=1:
               c=c+1
print(c//k)
