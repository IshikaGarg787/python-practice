rows=int(input("enter the number="))
for i in range(1,rows+1):
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(1,rows+1):    
    for j in range(rows-i):
        print('*',end=' ')
    print()

rows=int(input("enter the number="))
for i in range(1,rows+1):
    for j in range(rows-i):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(1,rows+1):
    for j in range(i):
        print(' ',end=' ')
    for j in range(rows-i):
        print('*',end=' ')
    print()
    
