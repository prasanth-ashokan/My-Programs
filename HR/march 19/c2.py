n,m,g=map(int,input().split())
t=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
c=0
for i in range(m):
    if(c==g):
        break
    elif(c<g):
        if i==0:
            if a[i]>t[i]:
                pass
            else:
                c=c+1
        else:
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
