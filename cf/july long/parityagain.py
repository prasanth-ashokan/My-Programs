for _ in range(int(input())):
    s=list()
    for __ in range(int(input())):
        q=int(input())
        s.append(q)
        w=len(s)
        for i in range(w):
            e=q^s[i]
            if e not in s and e!=0:
                s.append(e)
        d,r=0,0
        for i in s:
            a=bin(i)
            b=a.count('1')
            if b%2==0:
                d=d+1
            else:
                r=r+1
        print(d,r)
    
