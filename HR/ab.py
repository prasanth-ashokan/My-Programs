"""n=int(input())
a=[]
#a.append(1)
a=[int(i) for i in (input().split())]
b=[]
#b.append(1)
l=len(a)
def barray(l,o):
    b=[]
    for i in range(l):
        c=1
        for j in range(l):
            if i!=j:
                c=c*a[j]
        b.append(c)
    print(b[o-1])
for i in range(int(input())):
    p=input().split()
    p=[int(i) for i in p]
    o=p[1]
    if p[0]==0:
        a[1]=p[2]
        print(a)
    else:
        barray(l,o)"""
n=int(input())
l=[int(i) for i in (input().split())]
for k in range(int(input())):
    l1=[int(i) for i in (input().split())]
    B=[]
    a=1
    if(l1[0]==1):
        y=l1[1]
        j=1
        for i in l:
            j=j*i
        print(int(j/y)%((10**9)+7))
    else:
        t=l1[1]-1
        r=l1[2]
        l[t]=r
    
        
  
