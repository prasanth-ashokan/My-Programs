from collections import Counter
for x1 in range(int(input())):
    n,m,q=map(int,input().split())
  
    # Initialize matrix 
    ma= [] 

    # For user input
    u=0
    for i in range(n):          # A for loop for row entries 
        a =[] 
        for j in range(m):      # A for loop for column entries 
             a.append(u)
             u=u+1
        ma.append(a)
    c=[]
    for i in range(q):
        x,y=map(int,input().split())
        x=x-1
        y=y-1
        for j in range(m):
            c.append(str(ma[x][j]))
        for j in range(n):
            c.append(str(ma[j][y]))
    s=Counter(c)
    f=0
    for i in s:
        d=s[i]
        if d%2!=0:
            f=f+1
    print(f)
