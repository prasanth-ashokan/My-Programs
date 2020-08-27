from math import factorial as f
for i in range(int(input())):
    n=int(input())
    if n%2!=0:
        print("YES")
    elif n<10000:
        s=((n*n)+n)//2
        d=f(n)    
        r=d%s
        if r==0:
            print("YES")
        else:
            print(n)
    else:
        print("YES")
            
