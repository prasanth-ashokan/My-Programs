for _ in range(int(input())):
    sh,sm,eh,em=map(int,input().split())
    m=(60-sm)+em
    h=eh-sh-1
    if m>=60:
        s=m//60
        r=m%60
        h=h+s
        m=r     
    print(h,m)
    
