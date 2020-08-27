l=[1]
for i in range(2,1000):
    l.append((l[-1]+i+l[-1]*i)%1000000007)
print(l)
