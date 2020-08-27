s=input()
n=len(s)
m=n//2
if n%2==0:
    if s[:m]==s[m:] or s[:m]==s[:m-1:-1]:
        print("YES")
    else:
        print("NO")
else:
    m=m+1
    if s[:m-1]==s[m:] or s[:m-1]==s[:m-1:-1]:
         print("YES")
    else:
        print("NO")
        
