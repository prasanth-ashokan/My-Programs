def initializeDiffArray(A): 
    n = len(A) 
    D = [0 for i in range(0 , n + 1)] 
    D[0] = A[0]; D[n] = 0   
    for i in range(1, n ): 
        D[i] = A[i] - A[i - 1] 
    return D
def update(D, l, r, x): 
    D[l] += x 
    D[r + 1] -= x
def printArray(A, D):
    l=[]
    for i in range(0 , len(A)): 
        if (i == 0): 
            A[i] = D[i] 
        else: 
            A[i] = D[i] + A[i - 1] 
  
        l.append(A[i])
    return l
  
for x in range(int(input())):
    n=int(input())
    c=[]
    c.append(0)
    for i in input().split():
        c.append(int(i))
    z=[]
    z.append(0)
    for i in input().split():
        z.append(int(i))
    l=[0]*(n+1)
    d=initializeDiffArray(l)
    for i in range(1,n+1):
        q=i-c[i]
        if q<1:
            q=1
        w=i+c[i]
        if w>n:
            w=n
        update(d,q,w,1)
    l=sorted(printArray(l, d))
    z.sort()
    if(l==z):
        print("YES")
    else:
        print("NO")
        
