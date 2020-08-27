for _ in range(int(input())):
    n=int(input())
    l=[]
    s=""
    for i in range(n):
         a=input()
         s=''
         for i in a:
             if s.count(i)==0:
                 s=s+i
             else:
                 pass
         l.append(s)
    c=0
    for i in range(n):
        if i<n-1:
           for j in range(i+1,n):
               ss=len(set(l[i]).symmetric_difference(set(l[j])))
               print(ss)
               if len(set(l[i]).symmetric_difference(set(l[j])))==5:
                   c=c+1
               else:
                   pass
        else:
            pass
    print(c)
           
        
