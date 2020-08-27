import math 
mod=998244353
from collections import *
def fact(x):
    return math.factorial(x)
def ncr(n,r):
    return fact(n)/fact(r)*fact(n-r)
def xor(arr,n):
    res=0
    for i in arr:
        res=res^i
    return res
def getways(arr,n):
    xorway=xor(arr,n)
    if xorway==0:
        return 0
    ways=0;ans=0
    for i in arr:
        required=xorway^i
        if required<i:
            ways=int(ncr(i,i-required))
            ans+=ways
    return ways
for _ in range(int(input())):
    n=int(input())
    arrc=[int(i) for i in input().split()]
    for __ in range(int(input())):
        l,r=map(int,input().split())
        l=l-1
        c=list(Counter(arrc[l:r]).values())
        print(getways(c,len(c))%mod)

