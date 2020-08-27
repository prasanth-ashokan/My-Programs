for i in range(int(input())):
    for j in range(int(input())):
        l=[i for i in input().split()]
        p=sorted(l)
        print(*p)
