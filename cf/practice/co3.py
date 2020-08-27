for i in range(int(input())):
    l=[]
    n=int(input())
    a,b=map(int,input().split())
    e=1
    for j in range(1,n):
        c,d=map(int,input().split())
        if c in range(a,b):
            b=c
            a=d
        else:
            e=e+1
            b=c
            a=d
    print(e)
        
