t=int(input())
cnt=0
for i in range(t):
    r,x=map(int,input().split())
    dis=100*x
    par=2*22/7*r
    if(dis>=par):
        cnt+=1
print(cnt)
