a,b=0,7
for _ in range(int(input())):
    n=int(input())
    c=n-a
    d=b-n
    if c<=d:
        print("A")
        a=n
    else:
        print("B")
        b=n
    
