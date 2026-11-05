row=int(input('enter the number='))
for i in range(1,row+1):
    for j in range(1,row-i+1):
        print(' ',end=' ')
    for j in range(1,2*i):
        if j==1 or j==2*i-1 :
           print('*',end=' ')
        else:
           print(' ',end=' ')
    print()

for i in range(1,row+1):
    for j in range(1,row-i+1):
        print(' ',end=' ')
    for j in range(1,2*i):
        if j==1 or j==2*i-1 :
           print('*',end=' ')
        else:
           print(' ',end=' ')
    print()       
        
