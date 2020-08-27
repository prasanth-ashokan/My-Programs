for _ in range(int(input())):
    n,q=map(int,input().split(" "))
    c=1
    l=[]
    f=[]
    for i in input().split(" "):
        f.append(int(i))
        l.append([c,int(i)])
        c=c+1
    #print(l)
    for __ in range(q):
        la=[]
        b=0
        x1,x2,y=map(int,input().split(" "))
        for i in range(x1,x2+1):
            for j in range(y,y+1):
                     print(i,j)
                     b=b+1
        print(b)
