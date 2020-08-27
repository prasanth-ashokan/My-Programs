n=int(input())
p=n
for i in range(1,n+1):
    n=n-i
    if n==0:
        print("patlu")
        break
    o=2*i
    n=n-o
    print(n)
    i=i+1
    if n==0 or n<0:
        print("motu")
        break
    
