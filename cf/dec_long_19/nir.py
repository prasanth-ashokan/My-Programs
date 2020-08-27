from collections import *

for _ in range(int(input())):
    n=int(input())
    st=input()
    lis=[999999999]*26;flag=0
    #print(lis)
    dic1=defaultdict(lambda:-1)
    dic2=defaultdict(lambda:-1)
    alpha={chr(i):i-97 for i in range(97,123)}
    #print(alpha)
    #print(dic1)
    #print(dic2)
    for i in range(n):
        val=st[i]
        ind=alpha[st[i]]
        print(val,ind)
        if dic1[ind]==-1:
            dic1[ind]=i
        elif dic2[ind]==-1:
            dif=i-dic1[ind]
            print(dif)
            print(i,dic1)
            print(i,dic2)
            if dif==1:
                print(n-1)
                flag=1
                break
            dic1[ind]=i
            if lis[ind]>dif:
                lis[ind]=dif
        
    if not flag:
        fin=n-min(lis)
        if fin<0:
            print(0)
        else:
            print(fin)
    print(lis)
    

        
            
