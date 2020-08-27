def subString(s,l,r): 
    for i in range(r-l-1): 
        for len in range(l,r): 
            print(s[l:l+1]); 
for _ in range(int(input())):
    n,q=map(int,input().split())
    s=input()
    for i in range(q):
        l,r=map(int,input().split())
        subString(s,l,r)
        
        
    
