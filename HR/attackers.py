a=input()
l1=[i for i in a]
if l1[2]  in ["A","E","I","O","U","Y"]:
    print("invalid")
else:
    l1[2]="1"
    l1[6]="1"
    l=[int(i) for i in l1]
    if l[0]+l[1]%2!=0:
            if l[3]+l[4]%2!=0:
                if l[4]+l[5]%2!=0:
                    if l[7]+l[8]%2!=0:
                            print("valid")
                    
                    else:
                        print("invalid")
                else:
                    print("invalid")
            else:
                print("invalid")
    else:
        print("invalid")
