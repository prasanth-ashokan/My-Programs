s=[i for i in input()]
x,y=0,0
for i in s:
    if i=='L':
        x=x-1
    elif i=='R':
        x=x+1
    elif i=='U':
        y=y+1
    else:
        y=y-1
print(x,y)
        
