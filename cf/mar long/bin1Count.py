for i in range(0,100):
    print(i,bin(i)[2:],bin(i).count('1'))
'''for x in range(int(input())):
    n,q=map(int,input().split(" "))
    l=[int(i) for i in input().split(" ")]
    
    for i in range(q):
        e=0
        o=0
        w=int(input())
        for j in l:
            b=j^w
            c=(bin(b).count('1'))
            if c%2==0:
                e=e+1
            else:
                o=o+1
        print(e,o)'''
'''import math   
n=600
c=1
while(n!=0):
    c=c+1
    p=math.ceil(math.sqrt(n))
    print("p",p)
    r=2**p
    re=n-r
    print("re",re)
    n=re
print(c)
'''
