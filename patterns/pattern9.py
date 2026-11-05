side=int(input('enter the number='))
for i in range(1,side+1):
    for j in range(1,side+1):
        if i==side or i==1 or j==1 or j==side:
           print('*',end='')
        else:
            print(' ',end='')
    print()        
    
    
