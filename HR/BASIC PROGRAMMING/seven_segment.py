for _ in range(int(input())):
    d={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:4,8:7,9:6}
    n=[int(i) for i in input()]
    s=0
    for i in n:
        g=d[i]
        s=s+g
    t=s//2
    r=s-3
    if s%2==0:
        print(('1')*(t))
    else :
        if t>0:
            q=t-3
            print('7'+(('1')*(r//2)))
        
            
