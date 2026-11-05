st=input("enter the string=")
r=''
for i in st:
    if i.islower()==True:
       r+=(i.upper())
    else:
       r+=(i.lower())
print(r)    
   
