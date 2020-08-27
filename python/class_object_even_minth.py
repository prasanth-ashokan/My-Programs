l=[]
for _ in range(int(input())):
    name=input()
    dob=input()
    class Event:
        def __init__(self,name,dob):
            self.name=name
            self.dob=dob
        def checkDate(self):
            a=self.dob
            aa=a.split("/")
            md=int(aa[1])
            if md%2==0:
                print("Yes")
            else:
                print("No")
    a=Event(name,dob)
    a.checkDate()    
