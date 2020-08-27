n,m,g=map(int,input().split())
t=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
c=0
d=0
for i in range(1,n):
    d=d+1
    y=t[i]-t[i-1]
    for i in range(m):
        if c<=g:
            if a[i]>y:
                pass
            else:
                if d>len(a):
                    c=c+1
                else:
                    c=c+1
                    a[i]=1000
print(c)
