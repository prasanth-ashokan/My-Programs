r=[]
for i in range(1,9):
    for j in range(1,9,2):
        if i%2==0:
            j=j+1
        
        r.append(str(i)+str(j))
print(r)
