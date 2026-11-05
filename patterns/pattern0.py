rows=4
n=2
for i in range(1,rows+1):
    print(n)
    x=0
    while x==0:
     count=0
     for j in range(1,n+1):
      if n%j==0:
         count=count+1
         if count==2:
            x=1
     n+=1


    
    

