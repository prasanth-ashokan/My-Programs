import secrets
def add(A, B):
    c=0
    while B>0:
        c=c+1
        U = A^B
        V = A&B
        A = U
        B = V*2
    return c
'''for _ in range(int(input())):
    a=(input())
    a=int(a,2)
    b=(input())
    b=(int(b,2))
    print(add(a,b))'''

def add1(A, B):
    l=[2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384]
    c=0
    for y in range(20):
        if B==0:
            return c
            break
        else:
            c=c+1
            U = A^B
            V = A&B
            A = U
            B = V*2
            
            if B in l:
                print(c)
                print(A,B)
                print(bin(A)[2:])
                print(bin(B)[2:])
                
                A=bin(A)[2:]
                B=bin(B)[2:]
                al=len(A)
                fb=len(B)
                print(al,fb,c)
                A=A[:al-fb+1]
                #fa=fa[::-1]
                print(A,B)
                try:
                    print("b",fb)
                    i=A.rindex('0')
                    ii=len("A")-i
                    return ("u",i,ii,i+c)
                    break
                except:
                    return ("o",c+al-1,c,al)
                    break
            
            '''sb[-1]=2
            
            print(i)
        print(A,B,bin(A)[2:],bin(B)[2:])
    #print(l)'''
    return c
for _ in range(5):
    a=secrets.randbelow(100)
    #a=31
    aa=bin(a)[2:]
    #b=2
    an=a
    b=secrets.randbelow(2000)
    bb=bin(b)[2:]
    bl=len(bb)
    fa=bin(a^b)[2:]
    cc=a&b
    cc=cc*2
    bd=bin(cc)[2:]
    fb=len(bd)
    bn=b
    #print(add1((fa),fb,a,b),a,b)
    print(add(a,b),add1(a,b))
    print("\n")





































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
    
    
