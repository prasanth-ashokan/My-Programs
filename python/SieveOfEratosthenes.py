def sieve(n):
    prime=[True for i in range(n+1)]
    i=2
    while(i*i<=n):
        if prime[i]:
            for j in range(i*i,n+1,i):
                prime[j]=False
        i=i+1
    return prime
n=int(input())
p=sieve(n)
for i in range(2,n+1):
    if p[i]:
        print(i,end=" ")
        
