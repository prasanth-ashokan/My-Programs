n=int(input())
l=[int(i) for i in (input().split())]
for k in range(int(input())):
    l1=[int(i) for i in (input().split())]
    B=[]
    a=1
    if(l1[0]==1):
        y=l1[1]
        j=1
        for i in l:
            j=j*i
        print(int(j/y))
    else:
        t=l1[1]-1
        r=l1[2]
        l[t]=r
        
            
