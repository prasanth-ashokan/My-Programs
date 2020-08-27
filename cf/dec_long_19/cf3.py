l=[]
d=dict()
n=7
a='wertywe'
for j in range(n):
    i=a[j]
    if str(i) not in d:
        d[i]=dict(0,j)
    
print(d)
    
