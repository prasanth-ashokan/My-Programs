n,m,g=map(int,input().split())
t=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
c=0
while(c<n):
    for i in range(m):
        if i in range(n):
                p=t[i]-t[i-1]
                if p<a[i]:
                    pass
                else:
                    c=c+1
        else:
                 p=0
                 if p<a[i]:
                     pass
                 else:
                     c=c+1
print(c)

