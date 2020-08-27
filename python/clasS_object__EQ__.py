for i in range(int(input())):
    class User:
        def __init__(self,na,u,p,n):
            self.na=na
            self.u=u
            self.p=p
            self.n=n
        def __eq__(self,other):
            if isinstance(other,User):
                if self.n==other.n:
                    return True
                else:
                    return False
    a=User(input(),input(),input(),input())
    b=User(input(),input(),input(),input())
    if a==b:
        print("Equal")
    else:
        print("Not Equal")
