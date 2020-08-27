def prime(sr):
    sl=2
    sr=sr
    l=[]
    mul=[]
    m=[]
    pm=set()
    pm.add(1)
    sq=[]
    for i in range(sl,sr+1):
        ss=i*i
        if ss<=sr:
            pm.add(i*i)
        if i not in mul:
            l.append(i)
            for j in range(i*i,sr+1,i):
                mul.append(j)
                m.append(j*2)
                if j*2<=sr:
                    pm.add(j*2)
    return pm
o=sorted(list(prime(4)))
print(o)
import bisect
for i in range(int(input())):
    l,r=map(int,input().split())
    lb=bisect.bisect(o,l)
    lc=bisect.bisect(o,r)
    print(lb,lc)
