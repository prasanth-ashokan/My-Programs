n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
s=[]
for i in range(n):
    for j in range(n):
        if i!=j:
            s.append(a[i]+b[j])         
print(min(s))
