q='2203322'
t=q[0]
s=''
for i in (range(1,len(q))):
    if t==q[i]:
        s+='0'
    else:
        t=q[i]
        s+=t
print(q[0]+s)
        
