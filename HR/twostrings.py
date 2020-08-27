for _ in range(int(input())):
    a,b=map(str,input().split())
    l=[(i) for i in a]
    p=[i for i in b]
    l=sorted(l)
    p=sorted(p)
    s=''
    r=''
    for i in l:
        s=s+i
    for j in p:
        r=r+j
    if s==r:
        print("YES")
    else:
        print("NO")
