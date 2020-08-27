def iss(x): 
    return (x and (not(x & (x - 1))) )
for _ in range(int(input())):
    a=int(input())
    b=int(input())
    print(iss(a))
    print(iss(b))
