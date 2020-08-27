for x in range(int(input())):
    n,m=map(int,input().split())
    l=[]
    c=(n+m)//2
    
    a=c
    b=c
    if c==1 or c==8:
        l.append([c,c])
    else:
        l.append([c,c])
        for i in range(8):
            a=a+1
            b=b-1
            if a>0 and a<9 and b>0 and b<9:
                l.append([a,b])
        a=c
        b=c
        for i in range(8):
            a=a-1
            b=b+1
            if a>0 and a<9 and b>0 and b<9:
                l.append([a,b])    
        l.append([c,c])
    for i in range(1,9):
        
        if (i==1 or i==8) and i!=c:
            l.append([i,i])
        elif i!=c:
            a=i
            b=i
            l.append([i,i])
            for j in range(1,i-1):
                a=a+1
                b=b-1
                if a>0 and a<9 and b>0 and b<9:
                    l.append([a,b])
            a=c
            b=c
            for i in range(1,i-1):
                a=a-1
                b=b+1
                if a>0 and a<9 and b>0 and b<9:
                    l.append([a,b])    
            l.append([c,c])
                
    print(l)
        
