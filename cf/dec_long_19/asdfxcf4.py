def g(a,b):
        a=int(a,2)
        b=int(b,2)
        sum=a+b
        ss=str(bin(sum)[2:])
        a=bin(a)[2:]
        b=bin(b)[2:]
        sb=str(int(a)+int(b))
        
        if (sb==ss):
            return (1)
        
        if len(ss)!=len(sb):
            if len(ss)>len(sb):
                sb='0'*(len(ss)-len(sb))+sb
            else:
                ss='0'*(len(sb)-len(ss))+ss
        c=0
        for i in range(len(sb)):
            if sb[i]!=ss[i]:
                print(c)
            

        
