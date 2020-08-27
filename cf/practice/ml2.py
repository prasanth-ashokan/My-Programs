for _ in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split()]
    sp=0
    sn=0
    cp=0
    cn=0
    ll=len(l)
    for i in l:
        if i>0:
            sp=sp+i
            cp=cp+1
        else:
            sn=sn+abs(i)
            cn=cn+1
    if(cp==ll):
        print(cp,cp)
    elif(cn==ll):
        print(cn,cn)
    else:
        print(max(cp,cn),min(cp,cn))
