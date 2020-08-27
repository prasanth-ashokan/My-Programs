mod=1000000007
p=[10**i for i in range(50)]
def st(i):
    i=str(i)
    t=i[0]
    sq=''
    for j in (range(1,len(i))):
        if t==i[j]:
            sq+='0'
        else:
            t=i[j]
            sq+=t
    sq=i[0]+sq
    return(int(sq))
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
'''for _ in range(int(input())):
    k,a=map(int,input().split())
    h,b=map(int,input().split())
    s=0
    w=0'''

se=set()
for g in range(1):
    s=0
    w=0
    a=1
    l=[]
    r=[]
    ul=[]
    ur=[]
    for i in range(1,500):
        #x=g*(g+1)//2
        x=1
        z=i*(i+1)//2
        v=z-x
        u=count(i,s)
        e=st(i)
        ul.append(e)
        ur.append(u)
        if u!=i:
            l.append(i)
            r.append(u)
            
        w=w+count(i,s)
        print(g,i,"cor:",w%mod,"sod:",v,"differ:",v-w,"str:",e)
    
    
    
    
