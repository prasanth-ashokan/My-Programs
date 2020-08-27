"""_FAC_TABLE = [1, 1]
def factorial(n):
    if n < len(_FAC_TABLE):
        return _FAC_TABLE[n]

    last = len(_FAC_TABLE) - 1
    total = _FAC_TABLE[last]
    for i in range(last + 1, n + 1):
        total *= i
        _FAC_TABLE.append(total)

    return total"""
from math import factorial as f
for i in range(int(input())):
    n=int(input())
    s=((n*n)+n)//2
    print(f(n))    
    print(s)
    print((f(n)%s))
"""for i in range(int(input())):
    n=int(input())
    d=factorial(n)
    s=((n*n)+n)//2
    if d%s==0:
            print("YES")
    else:
            print("NO")"""

