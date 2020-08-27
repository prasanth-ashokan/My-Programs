n=int(input())
l1,l2,l3,l4=[],[],[],[]
for i in range(n):
    a,b,c,d=map(int,input().split())
    l1.append(a)
    l2.append(b)
    l3.append(c)
    l4.append(d)
l1=sorted(l1)
l2=sorted(l2)
l3=sorted(l3)
l4=sorted(l4)
for i in l1:
    if i in l3:
        n=n-1
print(n)
