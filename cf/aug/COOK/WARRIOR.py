for _ in range(int(input())):
    n,q=map(int,input().split())
    p=[int(i) for i in input().split(' ')]
    p=sorted(p)
    d=p[0]
    for i in range(q):
        x=int(input())
        c=0
        for j in p:
            if x>j:
                c=c+1
                x=2*(x-j)
            else:
                break
        print(c)
            
        
        
