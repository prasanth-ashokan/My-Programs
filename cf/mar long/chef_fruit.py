for i in range(int(input())):
    m,n=map(int,input().split(" "))
    f=[int(i) for i in input().split(" ")]
    p=[int(i) for i in input().split(" ")]
    l=[]
    for i in set(f):
        s=0
        for j in range(len(f)):
            if f[j]==i:
                s=s+p[j]
        l.append(s)
    print(min(l))
