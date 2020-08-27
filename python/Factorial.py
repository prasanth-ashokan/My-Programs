factorial=[1]
n=int(input())
for i in range(1,n+1):
    factorial.append(i*factorial[i-1])
print(factorial)
