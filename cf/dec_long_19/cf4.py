import secrets

def add1(A, B):
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
def sovi(a,b):
    if a==b:
        return 1
    elif b=='0':
        return 0
    elif a=='0':
        return 1
    
    else:
        a=int(a,2)
        b=int(b,2)
        sum=a+b
        ss=str(bin(sum)[2:])
        a=bin(a)[2:]
        b=bin(b)[2:]
        sb=str(int(a)+int(b))
        
        if (sb==ss):
            return (1)
        
        elif len(ss)!=len(sb):
            if len(ss)>len(sb):
                sb='0'*(len(ss)-len(sb))+sb
            else:
                ss='0'*(len(sb)-len(ss))+ss
            if sb[0]=='2':
               return(sb.count('2'))
            else:
                return(sb.count('2')+1)
        
        elif len(ss)==len(sb):
            if sb[0]=='2':
                return(sb.count('2'))
            else:
                return (sb.count('2')+1)
c=0
for _ in range(100):
    a=secrets.randbelow(30)
    aa=bin(a)[2:]
    an=a
    b=secrets.randbelow(20)
    bb=bin(b)[2:]
    bn=b
    if add1(a,b)==sovi(aa,bb):
        c=c+1
    if add1(a,b)!=sovi(aa,bb):
        sum=a+b
        ss=str(bin(sum)[2:])
        a=bin(a)[2:]
        b=bin(b)[2:]
        sb=str(int(a)+int(b))
        print(a,b)
        print(ss,sb)
        print(an,bn,add1(an,bn),sovi(aa,bb))
print(c)





































'''def gcd(c,d):
    if(d==0):
        return c
    else:
        return gcd(d,c%d)'''
'''sum=a+b
    #print(add1(a,b))
    #print(add2(a,b,a+b))'''
    #print("sum",a+b)
    #print("xor",a^b)
    #print("or",a|b)
    #print("and",a&b)
'''sb=str((int(bin(a)[2:])+int(bin(b)[2:])))
    ss=(bin(sum)[2:])
    if len(ss)>len(sb):
        sb='0'*(len(ss)-len(sb))+sb
    else:
        ss='0'*(len(sb)-len(ss))+ss
    print(ss)
    print(sb)'''
    
    
