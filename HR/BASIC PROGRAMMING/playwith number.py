n,q=map(int,input().split())
l=[i for i in input()]
for i in range(q):
    s,e=map(int,input().split())
    c=(s*(s+1))//2
    d=(e*(e+1))//2
    print(d,c)
    t=d-c+s
    print(t)
    y=e-s+1
    print(y)
    print(t//y)
