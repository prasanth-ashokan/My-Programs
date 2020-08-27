n=int(input())
l=[i for i in input()]
s=''
for i in l:
    if (i=='.'):
        s+='B'
    else:
        s+='H'
if s.count('B')>0 or len(l)==1 :
    if s[0]=='B' and s[n-1]=='B':
        print("NO")
    else:
        print("YES")
        print(s) 
else:
    print("NO")
    
        
