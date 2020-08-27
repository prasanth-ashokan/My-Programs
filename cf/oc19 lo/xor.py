import random
def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(str(random.randint(start, end))) 
  
    return res
def but(k):
        n=12
        l=[5665,54,67,7787,6478,54,67,78,3,8,1,6]
        for i in range(k):
            d1=i%n
            a=int(l[d1])
            d2=n-(i%n)-1
            b=int(l[d2])
            l[d1]=(a^b)
            s=''
            for i in l:
                s+=str(i)+' '
        return (s)
def sovi(k):
            n=12
            l=[5665,54,67,7787,6478,54,67,78,3,8,1,6]
            
            
            q=((k//n)%3)
            r=k%n
            if q==0:
                for j in range(r):
                    d1=j%n
                    a=(l[d1])
                    d2=n-(j%n)-1
                    b=(l[d2])
                    l[d1]=(a^b)
                if (n%2)!=0:
                    if k>n//2:
                        l[n//2]=0
                s=''
                for i in l:
                    s+=str(i)+' '
                return s
            elif q==1:
                for j in range(n):
                    d1=j%n
                    a=(l[d1])
                    d2=n-(j%n)-1
                    b=(l[d2])
                    l[d1]=(a^b)
                for j in range(r):
                    d1=j%n
                    a=(l[d1])
                    d2=n-(j%n)-1
                    b=(l[d2])
                    l[d1]=(a^b)
                s=''
                for i in l:
                    s+=str(i)+' '
                return s
            elif q==2:
                for j in range(n):
                    d1=j%n
                    a=int(l[d1])
                    d2=n-(j%n)-1
                    b=int(l[d2])
                    l[d1]=int(a^b)
                for j in range(n):
                    d1=j%n
                    a=int(l[d1])
                    d2=n-(j%n)-1
                    b=int(l[d2])
                    l[d1]=int(a^b)
                for j in range(r):
                    d1=j%n
                    a=(l[d1])
                    d2=n-(j%n)-1
                    b=(l[d2])
                    l[d1]=(a^b)
                s=''
                for i in l:
                    s+=str(i)+' '
                return s
for x in range(1):
    '''n,k=map(int,input().split())
    l=[(i) for i in input().split()]'''
    

    #k=10
    c=0
    for i in range(1,int(input())):
        #print(but(i))
        #print(sovi(i))
        #print('\n')
        
        if but(i)==sovi(i):
            c=c+1
            #print(i,but(i),sovi(i))
        else:
            print(i)
    print(c)       
        

        
