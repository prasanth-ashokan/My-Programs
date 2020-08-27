for _ in range(int(input())):
    n=int(input())
    if n%6==0 or n%6==1:
        if n%12<=6 and n%12 !=0:
            if n%3==1:
                print(n+11,"WS")
            else:
                print(n+1,"WS")
        else:
            if n%3==1:
                print(n-1,"WS")
            else:
                print(n-11,"WS")
    elif n%3==0 or n%3==1:
        if n%12<=6:
            if n%3==1:
                print(n+5,"AS")
            else:
                print(n+7,"AS")
        else:
            if n%3==1:
                print(n-7,"AS")
            else:
                print(n-5,"AS")
    else:
        if n%12<=6:
            if n%2==0:
                print(n+9,"MS")
            else:
                print(n+3,"MS")
        else:
            if n%2==1:
                print(n-9,"MS")
            else:
                print(n-3,"MS")
