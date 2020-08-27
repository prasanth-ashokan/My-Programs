l=[i for i in input()]
if len(l)!=10:
    print("Illegal ISBN")
else:
    s=0
    for i in range(1,11):
        s+=(i*int(l[i-1]))
    if s%11==0:
        print("Legal ISBN")
    else:
        print("Illegal ISBN")
    

