for _ in range(int(input())):
    p=int(input())
    l=[]
    s=[]
    for i in range(p):
        x,y=map(int,input().split())
        if i==0:
            s.append(x)
            s.append(y)
            l.append(s)
        else:
            for j in l:
                print(j,"j")
                for k in j:
                    print(k,"k")
                    if x and y not in j:
                        s=[]
                        s.append(x)
                        s.append(y)
                        l.append(s)
                    else:
                        if x not in j:
                            s.append(x)
                        else:
                            s.append(y)
    print(l)
