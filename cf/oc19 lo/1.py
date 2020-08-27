for x1 in range(int(input())):
    n,m,q=map(int,input().split())
    v=[]
    for i in range(n):          
        b=[]
        for j in range(m):       
             b.append(0)
        v.append(b)
    for i in range(q):
        x,y=map(int,input().split())
        x=x-1
        y=y-1
        for j in range(m):
            v[x][j]=v[x][j]+1
        for j in range(n):
            v[j][y]+=1
        c=0
        for i in range(n): 
            for j in range(m):
                if (v[i][j]%2)!=0:
                    c=c+1
                print(v[i][j], end = " ") 
            print()
        print(c)
    
