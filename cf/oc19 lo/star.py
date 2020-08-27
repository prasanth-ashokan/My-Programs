for x in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split()]
    dd=[]
    dd.append(0)
    for i in range(1,n):
        d=0
        for j in range(0,i):
            
            if l[j]%l[i]==0:
                d=d+1
        dd.append(d)
    print(dd)
