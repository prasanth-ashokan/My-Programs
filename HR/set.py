n=int(input())
a=[int(i) for i in input().split()]
m=int(input())
c=[int(i) for i in input().split()]
b=list()
f=c[-1]-a[-1]
g=c[0]-a[0]
for i in a:
    for j in c:
        w=j-i
        if w in range(g,f+1) and w not in b:
            b.append(w)
print(*b)
