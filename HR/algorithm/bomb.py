n=int(input())
l=[i for i in input().split()]
a=''
for i in l:
    a=a+i
m=0
for i in a.split('0'):
    b=len(i)
    if m<b:
        m=b
ma=0
for i in a.split('1'):
    b=len(i)
    if ma<b:
        ma=b
print(max(ma,m))
    
