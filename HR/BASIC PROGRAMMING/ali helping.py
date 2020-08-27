t=input()
a=[i for i in t]
if((int(a[0])+int(a[1]))%2==0):
    if((int(a[3])+int(a[4]))%2==0):
        if((int(a[4])+int(a[5]))%2==0):
            if((int(a[7])+int(a[8]))%2==0):
                if (a[2] not in ["A","E","I","O","U","Y"]):
                    print("valid")
                else:
                    print("invalid")
            else:
                print("invalid")
        else:
            print("invalid")
    else:
        print("invalid")
else:
    print("invalid")
            
            
        
