def dia(c):
    l=[]
    if c!=1 and c!=8:
        l.append([c,c])
    a=c
    b=c
    for i in range(c-1):
        a=a+1
        b=b-1
        if a>0 and a<9 and b>0 and b<9:
            l.append([a,b])
            l.append([b,a])
    l.append([c,c])
    return l
for _ in range(int(input())):
    n,m=map(int,input().split())
    nm=(n+m)//2
    ans=[]
    ans+=(dia((n+m)//2))
    for i in range(1,9):
        if nm!=i:
           ans+=(dia((i+i)//2)) 
    print(len(ans))
    for  i in ans:
        print(i[0],i[1])
