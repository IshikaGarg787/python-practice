num=int(input('enter the number'))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
print(count)
        
