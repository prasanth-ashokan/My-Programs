for _ in range(int(input())):
    a,b=map(str,input().split())
    f=0
    for i in a:
        if a.count(i)!=b.count(i):
            f=1
            break
    if f==1:
        print("NO")
    else:
        print("YES")
            
