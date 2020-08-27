for _ in range (int(input())):
    n=int(input())
    d=0
    l=[int(i) for  i in input().split()]
    s=0
    for i in l:
        s+=i
    tm=s/n
    for i in range(n):
        p=l[i]
        u=s-l[i]
        y=u/(n-1)
        if y==tm:
            d=1
            print(i+1)
            break;
    if d!=1:
        print("Impossible")
