for _ in range(int(input())):
    n,k=map(int,input().split())
    l=[]
    for i in input().split():
        l.append(int(i))
    while(len(l)>=k):
        m=[]
        for i in  range(0,len(l),k):
            if len(l[i:i+k])==k:
                m.append(sum(l[i:i+k]))
            else:
                for i in l[i:i+k]:
                    m.append(i)
        l=m
        m=[]
    s=""
    for i in l:
        s=s+str(i)+" "
    print(s)
            
        
