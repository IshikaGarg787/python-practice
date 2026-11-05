num=int(input('enter the number'))
length=len(str(num))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**length
    temp=temp//10
    
if sum==num:
    print('armstrong number')
else:
    print('not armstrong number')
    
