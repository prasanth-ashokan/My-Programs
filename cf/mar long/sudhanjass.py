t,s=map(int,input().split(" "))
for _ in range(t):
    n=int(input())
    c=[int(i) for i in input().split()]
    cf=[int(i) for i in input().split()]
    for __ in range(1):
        if c==cf:
            print("NO")
        else:
            h=set()
            c=sorted(c)
            d=sorted(cf)
            h.add(c[0])
            cc=0
            for i in range(n):
                if d[i]>c[i] and c[i] in h:
                    cc=cc+1
                    h.add(d[i])
                    h.add(c[i])
            if cc==n:
                print("YES")
            else:
                print("NO")
                
                
