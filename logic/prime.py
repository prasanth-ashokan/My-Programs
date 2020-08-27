def eratosthenes(n,l):
    multiples = []
    for i in range(2, n+1):
        if i not in multiples:
            l.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)
    return l
l=[]
eratosthenes(1000,l)
sovi=[]
sovi.append(2)
sovi.append(3)
sovi.append(5)
sovi.append(7)
se=set()
for i in range(6,1000):
    ii=i/6
    s=str(ii).split('.')
    a=s[1]
    
    if i%2!=0 and i%5!=0 and i%7!=0 and a in {'166666666666666', '1666666666666667', '3333333333333333', '166666666666668', '1666666666666665', '166666666666667', '8333333333333333', '8333333333333334', '8333333333333335', '833333333333333', '833333333333334'}:
        sovi.append(i)
print(sovi)
print(l)

        
            
