for _ in range(int(input())):
    l=[]
    s,x,y,z=map(int,input().split())
    l.append(x)
    l.append(y)
    l.append(z)
    l=sorted(l)
    k=[1,2,2]
    if x+y+z<=s:
        print(1)
    
    elif min(x,y,z)==s or( s==2 and k==l) or (s==3 and x==2 and y==2 and z==2):
        print(3)
    else:
        print(2)
