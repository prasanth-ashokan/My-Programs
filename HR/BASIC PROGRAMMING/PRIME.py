n=int(input())
l=[]
for i in range(97,123):
    c=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            c=1
    if c==0:
        l.append(i)
print(*l)
