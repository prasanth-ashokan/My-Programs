mod=1000000007
p=[10**i for i in range(50)]
def count(i,s):
    i=str(i)
    t=''
    for j in range(len(i)):
        if i[j]!=t:
            y=p[len(i)-j-1]
            t=i[j]
            q=int(i[j])*y
            s=s+q
    return s
for _ in range(int(input())):
    k,a=map(int,input().split())
    h,b=map(int,input().split())
    s=0
    w=0
    se=set()
    for i in range(a,b+1):
        for j in str(i):
            se.add(i)
        if len(se)==len(str(i)):
            w=w+i
        else:
            w=w+count(i,s)
    print(w%mod)
    
