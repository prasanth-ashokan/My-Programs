from itertools import combinations
n=int(input())
l=[int(i) for i in input().split()]
m=len(bin(max(l))[2:])
x=[]
y=[]
c=0
for i in l:
    b=bin(i).count('1')
    x.append(b)
    y.append(m-b)
    if b==m-b:
        c=0
if sum(x)==sum(y):
    c=0
cl=[i for i in range(n)]
for i in range(1,n+1):
    com=list(combinations(x,i))
    dom=list(combinations(y,i))
    for j in range(len(com)):
        if sum(com[j])==sum(dom[j]):
            c=c+1
rz=m-len(bin(c)[2:])
print(c)
l=x
s=1
for i in l:
  s+=s ^ i
print(s)
s=1
  
for i in l:
  s+=s or i
print(s)
s=1
  
for i in l:
  s+=s and i
print(s)
s=0

    
