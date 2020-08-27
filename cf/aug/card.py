def swap(s,a):
    if s[a]=='0':
        s[a]='1'
    elif s[a]=='1':
        s[a]='0'
        
for x in range(int(input())):
    s=[i for i in input()]
    i=0
    while(i<len(s)):
        
            q=s[i]
            if s[i]=='1':
                s[i]='w'
                if i!=(len(s)-1):
                        swap(s,i+1)
                if i!=0:
                        swap(s,i-1)
                        if s[i-1]=='1':
                            i=i-2

            i=i+1
    if('0' in s):
        print("LOSE")
    else:
        print("WIN")
                
        
                
                
            
            
        
