l=[i for i in input().split(" ")]
ans=[]
for i in l:
    d=0
    da=0
    try:
        a=int(i)
        d=1
    except:
        d=0
    if d==1:
        a=str(a)
        e=len(a)
        if len(a)==1:
            ans.append(int(a)+1)
        else:
            q=int(a[0])
            w=int(a[1])
            if q>w:
                m=q
                mm=w
            else:
                m=w
                mm=q
            bv=((m+1)*mm)+m
            ans.append(bv)
    else:
        if len(i)==1:
            o=ord(i)-55
            ans.append(o)
        else:
            ao=ord(i[0])-55
            bo=ord(i[1])-55
            if ao in range(10,36):
                if bo in range(10,36):
                    if ao>bo:
                        m=ao
                        mm=bo
                    else:
                        m=ao
                        mm=bo
                    bv=((m+1)*mm)+m
                    ans.append(bv)
                else:
                    ap=ao
                    d=int(i[1])
                    bv=(ap*(ap+1))+d
                    ans.append(bv)
            else:
                    ap=bo
                    d=int(i[0])
                    bv=(d*(ap+1))+ap
                    ans.append(bv)           
print(min(ans))
            
     
     

