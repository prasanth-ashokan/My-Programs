h=int(input())
l=[int(i) for i in input().split()]
v=[int(i) for i in input().split()]
d=[i for i in input().split()]
for ii in range(5):
    for i in range(4):
        if l[i]>0 and l[i]<h:
            if d[i]=='U':
                l[i]=l[i]+v[i]
            else:
                l[i]=l[i]-v[i]
    print(ii,l,[l[0],l[2],l[3]],[l[0],l[2],l[1]])
