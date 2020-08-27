n=int(input())
a=1
l=[int(i) for i in input().split()]
for i in l:
    print(i)
    a*=int(i)
print(a%(1000000007))
