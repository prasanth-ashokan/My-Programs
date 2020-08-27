'''import itertools 
  
def findsubsets(s, n): 
    return list(itertools.combinations(s, n)) 
def convert(set): 
    return list(set)
for j in range(10):
    c=0
    n,k=map(int,input().split())
    l=[int(i) for i in input().split(" ")]
    for i in range(k+1):
        m=(findsubsets(l, i))
        p=[]
        for i in m:
            if(list(i)==list(set(i))):
               c=c+1
    print(c)

    '''
from collections import *
from sys import stdin, stdout
for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    st=stdin.readline()
    lis=[999999999]*26;flag=0
    dic1=defaultdict(lambda:-1)
    dic2=defaultdict(lambda:-1)
    alpha={chr(i):i-97 for i in range(97,123)}
    for i in range(n):
        val=st[i]
        ind=alpha[st[i]]
        if dic1[ind]==-1:
            dic1[ind]=i
        elif dic2[ind]==-1:
            dif=i-dic1[ind]
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
        
    

        
            
