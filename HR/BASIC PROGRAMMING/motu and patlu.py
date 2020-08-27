n=int(input())
b=n
c=0
d=0
for i in range(1,n+1):
    q=b-i
    b=q
    if q<=0:
        print("Patlu")
        break;
    q=b-(2*i)
    b=q
    if q<=0:
        print("Motu")
        break
     
    
