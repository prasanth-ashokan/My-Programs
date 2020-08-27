import math
prime=[]
for i in range(2,100000):
    f=0
    for j in range(2,int(math.sqrt(i))+1):
        if(i%2==0):
            f=1
    if (f==0):
        prime.append(i)
print(prime)
