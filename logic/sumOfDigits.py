import bisect
def sod(n):
    s=0
    l=[]
    for  i in range(1,n+1):
        s=s+i
        l.append(s)
    return (l)
n=6
l=sod(n)
a=[-3,2,3,-4,3,1]
ts=sum(a)
q=-99999999999999999
for i in range(n):
    r=n-i
    bs=bisect.bisect_right(l,r)
    ti=l[bs-1]
    qq=sum(a[i:i+ti])
    print(i,qq,ts)
    if qq>q:
        q=qq
    ts=ts-a[i]
