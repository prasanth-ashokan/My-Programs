for _ in range(int(input())):
    s=0
    n=int(input())
    for i in range(1,int((n/2)+1)):
        if(n%i==0):
            s=s+i
        else:
            continue
    print(s)
    s=0
