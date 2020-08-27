n=int(input())
pascal=[]
for i in range(n+1):
    temp=[]
    for j in range(i+1):
        if j==0 or i==j:
            val=1
        else:
            val=pascal[i-1][j-1]+pascal[i-1][j]
        temp.append(val)
    pascal.append(temp)
for i in pascal:
    print(i)
        
