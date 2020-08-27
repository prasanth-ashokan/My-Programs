l=[]
s={}
for _ in range(int(input())):
    a=int(input())
    l.append(a)
    m=min(l)
    h=[]
for j in range(2,m+1):
    u=l[0]%j
    c=0
    y=l[1]%j
    if u==y:
        for k in range(len(l)):
            if l[k]%j==u:
                c=c+1
            else:
                continue
        if(c==len(l)):
            h.append(j)
        else:
            continue
    else:
        continue
for b in h:
    print(b,end=' ')
        
        
        
        
