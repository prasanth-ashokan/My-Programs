import math
def product(number):
    n=number
    p=1
    while(number!=0):
        temp=number%10
        p=p*temp
        number=number//10
    return p
def perfect(number):
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return 1
    else:
        return 0
a,b,k=map(int,input().split())
for i in range(a,b+1):
    if '0' not in str(i):
        if perfect(product(i)):
            print(i)

