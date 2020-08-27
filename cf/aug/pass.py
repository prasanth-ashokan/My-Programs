for x in range(int(input())):
    s=input()
    c=1
    l=[]
    c=1
    l=[0 for i in range(len(s))]
    k=[]
    f=0
    n=0
    for i in range(len(s)):
        if s[i]=='+':
            f=f+1
            l[i]=f
            n=0
        else:
            n=n+1
            l[i]=n
            f=0
    print(l)
            
            
            
        
