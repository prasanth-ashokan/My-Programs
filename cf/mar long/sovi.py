from sys import stdin, stdout
for x in range(int(stdin.readline())):
    n,q=map(int,input().split(" "))
    l=[int(i) for i in stdin.readline().split(" ")]
    for i in range(1):
        e1=0
        o1=0
        for j in l:
            r=j^1
            c1=bin(r).count('1')
            if c1%2==0:
                e1=e1+1
            else:
                o1=o1+1
    for i in range(q):
        w=int(stdin.readline())
        wc=bin(w).count('1')
        if wc%2==0:
            print(o1,e1)
        else:
            print(e1,o1)
        
