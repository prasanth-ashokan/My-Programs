def same():
    l=[]
    for i in range(2,9):
            l.append([i,i])
            a=i
            b=i
            if i>1 and i<5:
                ll=[]
                rr=[]
                for j in range(i-1):
                    a=a+1
                    b=b-1
                    ll.append([a,b])
                    rr.append([b,a])
                l=l+ll+rr
            elif i>4:
                ll=[]
                rr=[]
                for j in range(8-i):
                    a=a+1
                    b=b-1
                    ll.append([a,b])
                    rr.append([b,a])
                l=l+ll+rr
            if i!=8:
                l.append([i,i])
    print(len(l))
    for i in l:
        print(i[0],i[1])
for x in range(int(input())):
    #n,m=map(int,input().split())
    for y in range(1,9):
        for v in range(1,9,2):
            if y%2==0:
                v=v+1
            n=y
            m=v
            c=1
            l=[]
            f=0
            if n==1 and m==1:
                same()
            else:
                ll=[]
                if n==2 and m==6:
                    ll.append([1,7])
                if n==3 and m==7:
                    ll.append([2,8])
                a=n
                b=m
                for i in range(8):
                    a=a+1
                    b=b-1
                    if a>0 and a<9 and b>0 and b<9:
                        ll.append([a,b])
                    else:
                        break
                ll.append([n,m])
                for i in ll:
                    if i[0]==i[1]:
                        c=i[0]
                a=c
                b=c
                for i in range(8):
                    a=a+1
                    b=b-1
                    if a>0 and a<9 and b>0 and b<9:
                        ll.append([a,b])
                    else:
                        break
                ans=ll
                l=[]
                for i in range(1,9):
                    if i!=c:
                        if i!=1:
                            l.append([i,i])
                        a=i
                        b=i
                        if i>1 and i<5:
                            ll=[]
                            rr=[]
                            for j in range(i-1):
                                a=a+1
                                b=b-1
                                ll.append([a,b])
                                rr.append([b,a])
                            l=l+ll+rr
                        elif i>4:
                            ll=[]
                            rr=[]
                            for j in range(8-i):
                                a=a+1
                                b=b-1
                                ll.append([a,b])
                                rr.append([b,a])
                            l=l+ll+rr
                        if i!=8:
                            l.append([i,i])
                g=[]
                g.append([c,c])
                q=ans+g+l
                #print(q)
                #print(len(q))
                s=[]
                for i in q:
                    s.append(str(i[0])+str(i[1]))
                    #print(i[0],i[1])
                if len(set(s))!=32:
                    print(y,v,len(set(s)))
                '''l=[]
                r=[]
                s=[]
                c=(n+m)//2
                for i in range(c):
                    if [c-i,c+i] not in r:
                        if i!=0:
                            r.append([c-i,c+i])
                    if [c+i,c-i] not in s:
                        if n!=c+i and m!=c-i:
                            s.append([c+i,c-i])
                print(r,s)'''
            
            
        
