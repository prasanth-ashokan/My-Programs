def add1(A,B):
    l=[]
    c=0
    while B>0:
        c=c+1
        U = A^B
        V = A&B
        A = U
        B = V*2
        l.append([A,B])
    #print(l)
    return c
y=[1,2,4,8,16,32,64,128,256,512]
print(add1(21,17))
l=[0]
b,a=map(str,"1011000 1002112".split(" "))
print(a)
#a=int(a)
for i in a:
    l.append(int(i))
s=(l[::-1])
'''if int(s[0])>1:
    s[1]=s[1]+s[0]
    s[0]=0
for i in range(1,len(s)-1):
    if s[i]>2:
        s[i+1]=s[i]+s[i+1]
        s[i]=0
    print(i,s[::-1])'''
t=[]
for i in range(0,len(s)):
    t.append(s[i]*pow(2,i))
print(t)
c=0
for i in range(0,len(s)):
    if t[i]>y[i]:
        c=c+1
        t[i+1]=t[i]+t[i+1]
        if y[i+1]==t[i]+t[i+1]:
            if t[i+1]==0:
                t[i+1]=t[i]+t[i+1]
            else:
                
                
            
        t[i]=0
        if i>len(a)-2:
            c=c+1
print(t,c)
