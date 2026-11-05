start=int(input('enter the range to start='))
stop=int(input('enter the range to stop='))
sum=0
for i in range(start,stop+1):
  count=0
  for j in range(1,i+1):
     if i%j==0:
       count=count+1
       
  if count==2:
      print(i,end=' ')
