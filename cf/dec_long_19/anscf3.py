for _ in range(int(input())):
    a=input()
    b=input()
def sovi(a,b)
    if b=='0':
        print(0)
    elif a=='0':
        print(1)
    else:
        a=int(a,2)
        b=int(b,2)
        sum=a+b
        ss=str(bin(sum)[2:])
        a=bin(a)[2:]
        b=bin(b)[2:]
        sb=str(int(a)+int(b))
        
        if (sb==ss):
            print(1)
        
        elif len(ss)!=len(sb):
            if len(ss)>len(sb):
                sb='0'*(len(ss)-len(sb))+sb
            else:
                ss='0'*(len(sb)-len(ss))+ss
            if sb[0]=='2':
                print(sb.count('2'))
            else:
                print(sb.count('2')+1)
        
        elif len(ss)!=len(sb):
            if sb[0]=='2':
                print(sb.count('2'))
            else:
                print(sb.count('2')+1)
        #print(ss)
        #print(sb)
   
        
