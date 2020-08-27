from collections import Counter as c
def c_factor(n,ll):
    for i in range(1,n+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c=c+1
            else:
                pass
        ll.append(c)
    return ll
t,n=map(int,input().split())
l=[]
ll=[]
d={}
for i in range(t):
    l.append(int(input()))
c_factor(n,ll)
p=sorted(ll)
e=list(most_common)
u=[]
for x in l:
    g=0
    d=x-1
    m=ll[d]
    for y in p:
        if y<m:
            g=g+1
        else:
            pass
    print(g)
    

        
    
