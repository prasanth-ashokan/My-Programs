for _ in range(int(input())):
    l,q=[],[]
    n=int(input())
    for i in range(n):
        a=input()
        b=a[0:n//2].count('1')
        c=a[(n//2):].count('1')
        l.append(b)
        q.append(c)
    if sum(l)==sum(q):
        print(0)
    else:
        min=abs(sum(l)-sum(q))
        for i in range(n):
            m=abs((sum(l)-l[i]+q[i])-(sum(q)+l[i]-q[i]))
            if m<min:
                min=m
        print(min)
                
            
    
        
