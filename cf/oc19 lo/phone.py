for x1 in range(int(input())):
    n=int(input())
    l=[]
    l.append(9999999)
    for i in input().split():
        l.append(int(i))
    c=1
    for i in range(2,n+1):
        if i-5<0:
            r=i//5
        else:
            r=i-5
        if l[i]<min(l[r:i]):
            c=c+1
    print(c)
