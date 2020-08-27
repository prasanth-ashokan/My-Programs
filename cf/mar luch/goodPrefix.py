for _ in range(int(input())):
    xk={'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    s=input();k,x=map(int,input().split());gp='';f=0
    for i in s:
        xk[i]=xk[i]+1
        if xk[i]<=x:
            gp=gp+i
        else:
            if k==0:
                print(len(gp));f=1;break
            else:
                k=k-1
    if f==0:
        print(len(gp))
