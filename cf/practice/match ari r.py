for _ in range(int(input())):
    n,m=map(int,input().split())
    c=1
    while(n!=0 and m!=0):
        if n>=m:
            while(n<=m):
                n=n-m
        else:
            while(m<=n):
                m=m-n          
        print(n,m)
    if c%2!=0:
        print("Rich")
    else:
        print("Ari")
    
