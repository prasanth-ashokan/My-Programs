import string 
import random
import secrets
def sovi(a,n,st):
    ma=0
    for i in range(0,n):
        for j in range(i+1,n):
            if(a[i]==a[j]):
                k=a[:i]+a[i]+a[j+1:]
                l=len(k)
                if l>ma:
                    ma=l
                    st=k
    return (ma)
            
def qwe(a,n,ld):
    f=0
    a=['a','b','b','c']
    for i in (a):
        if(a.count(i)>1):
            y=0
            for j in range(a.count(i)-1):
                fi=a.index(i)
                a[fi]=-1
                ni=a.index(i,fi+1)
                y=ni+1
                dbi=ni-fi
                ld.append(dbi)
                f=1
    if f==0:
        return (0)
    else:
        return (n-(min(ld)))
for _ in range(int(input())):
    N=secrets.randbelow(20)
    st=''
    ld=[]
    a= ''.join(random.choices(string.ascii_uppercase, k = N))
    n=len(a)
    if(sovi(a,n,st)!=qwe(a,n,ld)):
        print(sovi(a,n,st),qwe(a,n,ld),a,n,st,ld)

