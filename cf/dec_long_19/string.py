import string 
import random
import secrets
from collections import *
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
            
def qwe(st,n):
    lis=[999999999]*26
    dic1=defaultdict(lambda:-1)
    dic2=defaultdict(lambda:-1)
    alpha={chr(i):i-97 for i in range(97,123)}
    for i in range(n):
        val=st[i]
        ind=alpha[st[i]]
        if dic1[ind]==-1:
            dic1[ind]=i
        elif dic2[ind]==-1:
            dif=i-dic1[ind]
            if dif==1:
                return (n-1)
            dic1[ind]=i
            if lis[ind]>dif:
                lis[ind]=dif
    
    if (n-min(lis))<0:
        return 0
    else:
        return (n-min(lis))
for _ in range(int(input())):
    N=secrets.randbelow(20)
    st=''
    a= ''.join(random.choices(string.ascii_lowercase, k = N))
    n=len(a)
    l=[]
    ld=[]

    for i in a:
        l.append(i)
    if(sovi(a,n,st)!=qwe(a,n)):
        print(sovi(a,n,st),qwe(a,n),a)

