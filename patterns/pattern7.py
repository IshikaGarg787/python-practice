rows=8
a=1
for i in range(1,rows+1):
    for j in range(i):
        if j==0 or j==i-1 or i==rows:
            print(a,end='')
        else:
            print(' ',end='')
        a=(a+1)%10
        #if a>9:
           #a=0
        
    print()
    
    
    
