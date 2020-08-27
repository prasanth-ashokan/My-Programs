import math
for _ in range(int(input())):
    n=int(input())
    k=int(input())
    a=k%n
    b=n-a
    if a==b:
        print(n-1)
    else:
        print(min(a,b)*2)
        
        
            
