def fstsum(str1, str2): 
    if len(str1)> len(str2): 
        temp = str1 ;str1 = str2 ;str2 = temp 
    str3 = "" 
    n1 = len(str1) 
    n2 = len(str2) 
    diff = n2 - n1 
    carry = 0
    for i in range(n1-1,-1,-1): 
        sum = ((ord(str1[i])-ord('0')) +
                int((ord(str2[i+diff])-ord('0'))) + carry) 
        str3 = str3+str(sum%10 ) 
        carry = sum//10
    for i in range(n2-n1-1,-1,-1): 
        sum = ((ord(str2[i])-ord('0'))+carry) 
        str3 = str3+str(sum%10 ) 
        carry = sum//10 
    if (carry): 
        str3=str3+str(carry)
    str3 = str3[::-1] 
    return str3
def sumNatural(n):
    sum = (n*(n+1))//2
    return sum
def suminRange(l, r): 
    return sumNatural(r) - sumNatural(l-1)
def fun(s):
    c=0;cr=s[0];n=len(s);i=1;
    while(i<n):
        if cr==s[i]:
            s[i]='0';i+=1
        else:
            cr=s[i];i+=1
    return int(''.join(s))
xmen=['45'];xmen1=[]
xmens='49';xmen1s='50'
for i in range(100005):
    xmen.append(xmens)
    xmens+='9'
prev=[];
def find(x):
    c=len(x)
    if c<3:
        return '0'
    i=c-1-2
    if i==0:
        return xmen[i]
    else:
        return xmen[i]+fstsum(xmen[i],'1')
def dfind(y,x):
    cal='1'+'0'*(len(x)-1);fb=int(x[0]);st=int(y[0]);
    inc=find(cal);ans='0';
    for i in range(st,fb):
        ans=fstsum(ans,(str(i)+inc))
    return ans
def dfind1(y,x,pre):
    global prev,cst;cal='1'+'0'*(len(x)-1);fb=int(x[0]);st=int(y[0]);
    inc=find(cal);ans=str(inc);ans2=0;
    if len(prev)!=0:
        for prev1 in prev:
            ans2+=prev1[0]*fb*(int(cal))*10**(prev1[1]-1)
    for i in range(st,fb):
        ans=fstsum(ans,(str(i)+inc))
    if str(pre)<str(fb):
        if str(fb)<='4':
            ans=str(pre)+'0'+ans
        else:
            ans=str(pre)+ans
    if str(pre)==str(fb):
        ans=fstsum(ans,str(int(pre)*int(cal)));
        prev.append([int(pre),len(x)])
    return int(ans)+ans2
pre=0
def main1(x):
    global prev,pre;prev=[];n=x;ans1='0';fst='1'+'0'*(len(n)-1)
    ans=find(fst);
    ans=fstsum(ans,str(dfind(fst,str(int(n[0])*int(fst)))))
    pre=n[0];n=n[1:];
    ans1=fstsum(ans1,ans)
    while(len(n)>2):
        fst='1'+'0'*(len(n)-1)
        if n[0]=='0':
            finder='0'
        else:
            finder=str(n[0])+'0'*(len(n)-1)
        ans1=fstsum(ans1,str(dfind1(fst,finder,pre)))
        pre=n[0];n=n[1:]
    return int(ans1)
def main2(xax,yax):
    l=xax;r=yax;global pre;
    lb=l[:-2]+'00';rb=r[:-2]+'00';s1,s2=0,0;
    if int(l)>=100:
        s1=(main1(lb));
        for x1 in range(int(lb)+1,int(l)+1):
            str1=[j for j in str(x1)]
            if len(str1)!=len(set(str1)):
                x2=fun(str1)
                if x2!=x1:
                    s1+=(x1-x2)
        if len(set(l[-2:]))==1:
            s1-=int(l[-2])
        if pre==l[-2]:
            s1-=int(pre)*10
        if len(prev)!=0:
            for nw in prev:
                s1-=int(nw[0])*10**(nw[1]-1)
    else:
        for x1 in range(1,int(l)+1):
            str1=[j for j in str(x1)]
            if len(str1)!=len(set(str1)):
                x2=fun(str1)
                if x2!=x1:
                    s1+=(x1-x2)
                else:
                    s1+=x1
        if len(set(l[-2:]))==1 and len(l[-2:])==2:
            s1-=int(l[-2])
    if int(r)>=100:
        s2=(main1(rb))
        for x1 in range(int(rb)+1,int(r)+1):
            str1=[j for j in str(x1)]
            if len(str1)!=len(set(str1)):
                x2=fun(str1)
                if x2!=x1:
                    s2+=(x1-x2)
    else:
        for x1 in range(1,int(r)+1):
            str1=[j for j in str(x1)]
            if len(str1)!=len(set(str1)):
                x2=fun(str1)
                if x2!=x1:
                    s2+=(x1-x2)
                else:
                    s2+=x1
    return ((suminRange(1, int(r))-suminRange(1, int(l))-(s2-s1)))+int(l)
def main3(alp,gam):
    mod=(10**9)+7
    return main2(alp,gam)%mod
for _ in range(int(input())):
    nl,lx=map(str,input().split())
    nr,rx=map(str,input().split())
    print(main3(lx,rx))
