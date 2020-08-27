import bisect
for _ in range(int(input())):
    n=int(input())
    l=[int(ord(i)) for i in input()]
    p=[67,71,73,79,83,89,97,101,103,107,109,113]
    s=''
    for i in l:
        mi=999
        for j in p:
            c=abs(j-i)
            if c<mi:
                mi=c
                f=j
        s+=chr(f)
    print(s)
        
   
        
