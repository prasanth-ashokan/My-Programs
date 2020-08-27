for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    l=[]
    for i in range(n):
        l.append((a[i]*20)-(b[i]*10))
    if max(l)>0:
        print(max(l))
    else:
        print("0")
        
