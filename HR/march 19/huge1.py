n=int(input())
p,q,u=0,0,0
l1,l2,l3=[],[],[]
s=n//2
e=s-1
for i in range(n):
    a,b,r=map(int,input().split())
    l1.append(a)
    l2.append(b)
    l3.append(r)
l1=sorted(l1)
l2=sorted(l2)
l3=sorted(l3)
print((min(l1[s]//2,l1[e]//2)),(min(l2[s]//2,l2[e]//2)),(min(l3[s]//2,l3[e]//2)))
