for _ in range(int(input())):
    a,b=map(str,input().split())
    l=[]
    for i in a:
        l.append((i))
    for i in b:
        l.append((i))
    nl=l
    l=sorted(l)
    n=len(l)
    if n==4:
        if nl[0]<nl[3]:
            
        s=int(l[3]+l[0])+int(l[1]+l[2])
    if n==3:
        s=int(l[2]+l[1])+int(l[0])
    if n==2:
        s=int(l[0])+int(l[1])
    print(s)
