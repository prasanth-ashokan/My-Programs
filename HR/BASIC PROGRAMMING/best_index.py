from itertools import accumulate   
def cumulativeSum(l): 
      return (list(accumulate(l)))
n=int(input())
l=[int(i) for i in input().split()]
f=0
ll=[]
s=0
max=0
for i in range(0,n):
    c=i
    d=0
    for j in range(1,n):
        if f==0:
            if len(l[c:c+j])==j:
                r=cumulativeSum(l[c:c+j])
                s=+r[-1]
                d+=s
        
            c+=j
    if d>max:
        max=d
print(max)


        
        
    
    
