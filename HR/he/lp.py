n,x=map(int,input().split())
l=[int(i) for i in (input().split())]
c=0
for i in l:
    print(i)
    if x>0:
        c=c+1
        x=x-i
        print(x)
    else:
        break
print(c)
