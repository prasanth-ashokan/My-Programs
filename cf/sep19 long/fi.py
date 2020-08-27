for x in range(int(input())):
        n=int(input())
        if  n==3 or n==4:
             print(1)

        else:
            a=[0,1]
            for y in range(2,n-1):
                t=a[y-2]
                r=a[y-1]
                a.append((t+r))
                r=a
            while(len(a)>=2):
                l=a
                a=[]
                for i in range(1,len(l),2):
                    a.append(l[i])
            print(a[0]%10)

        
            
            
            
