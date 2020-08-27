from itertools import permutations 
import bisect
a,b=map(str,input().split(" "))
a=[(i) for i in a]
b=int(b)
perm = permutations(a)
ac=[]
for i in list(perm):
    t=''.join(list(i))
    ac.append(int(t))
ac=sorted(ac)
ind=bisect.bisect(ac,b)
try:
    print(ac[ind])
except:
    print(-1)
    
