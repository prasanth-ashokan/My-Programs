for _ in range(int(input())):
    n,k=map(int,input().split())
    a=(n//k)%k
    if a==0:
        print("NO")
    else:
        print("YES")
    

