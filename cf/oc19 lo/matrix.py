from collections import Counter
for x1 in range(int(input())):
    n,m,q=map(int,input().split())
    c=[]
    d=[]
    for i in range(q):
        
        x,y=map(int,input().split())
        x=x-1
        y=y-1
        k=str(x)+"#"+str(y)
        for j in range(max(n,m)):
                if j<n:
                    o=str(j)+"#"+str(y)
                    if o!=k and o not in c:
                        c.append(o)
                    elif o in c and o!=k:
                        c.remove(o)
                    
                if j<m :
                    o=str(x)+"#"+str(j)
                    if o!=k and o not in c:
                        c.append(o)
                    elif o in c and o!=k:
                        c.remove(o)
    print(len(c))
'''if i%2==0:
            for j in range(max(n,m)):
                if j<n:
                    o=str(j)+"#"+str(y)
                    if o!=k:
                        c.append(o)
        
                    
                if j<m:
                    o=str(x)+"#"+str(j)
                    if o!=k:
                        c.append(o)
        else:
            for j in range(max(n,m)):
                if j<n:
                    o=str(j)+"#"+str(y)
                    if o!=k and o not in c:
                        c.append(o)
                    if o in c:
                        c.remove(o)
                    
                if j<m:
                    o=str(x)+"#"+str(j)
                    if o!=k:
                        c.append(o)
                    if o in c:
                        c.remove(o)
            
                
    print(c)
    cc=Counter(d)
    h=0
    for i in cc:
        if cc[i]%2!=0:
            h=h+1
    print(h) '''  
