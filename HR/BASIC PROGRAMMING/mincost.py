n,k=map(int,input().split())
l=[int(i) for i in input().split()]
t=[0 for i in range(n)]
for i in range(n):
    min=99999
    print("i",i)
    for j in range(i,i+k):
        print("j",j)
        if l[i]>0 and l[j]<0:
            t[i]=l[j]*l[i]
            t[j]=l[i]
            print(t[i],i)
print(t)
            
            
