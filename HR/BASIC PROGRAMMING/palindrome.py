n=[i.split() for i in input()]
l=len(n)
for i in range(0,l//2):
    c=0
    if n[i]!=n[l-i-1]:
        c=1
    if c==1:
        print("NO")
        break
if c==0:
    print("YES")

        
