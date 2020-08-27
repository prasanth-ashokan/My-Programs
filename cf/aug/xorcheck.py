def xor(x):
    x1=x[0]
    for i in range(1,len(x)):
        x1^=x[i]
    return x1
for _ in range(1):
    l=[1,9,159,179]
    n=len(l)
    
    c=0
    for i in range(0,n):
        for j in range(i,n):
            for k in range(j,n):
                x,y=l[i:j],l[j:k+1]
                if len(x)>0 and len(y)>0:
                    print(i,j,k)
                    if xor(x)==xor(y):
                        c+=1
    print(c)
            
