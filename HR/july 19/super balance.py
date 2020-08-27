import math
for _ in range(int(input())):
    su=""
    c=0
    max=0
    k=[]
    l=[ord(i)  for i in input()]
    for i in l:
        if i==40:
            c=c+1
        else:
            k.append(c)
            if c>=max:
                max=c
            c=0
    u=k.count(1)
    if (max !=1 or len(l) in[2,4]):
            if (k[0]>=u):
                print(2*max)
            else:
                print(2*max+2)
    else:
        if (((len(l)//2)%2)==0):
            print(len(l)//2)  
        else:
              print((len(l)//2)+1)
    
        
