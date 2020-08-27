for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    a=(a*60)+b
    c=(c*60)+d
    print(a,c)
    print(c-a)
    h=(c-a)//60
    m=(c-a)%60
    print(h,m)
