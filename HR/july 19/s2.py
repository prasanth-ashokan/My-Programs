for _ in range(int(input())):
    s=input()
    n=len(s)
    l=s[:n//2]
    q=s[n//2:]
    a=l.count('(')
    b=q.count(')')
    print(min(a,b)*2)
