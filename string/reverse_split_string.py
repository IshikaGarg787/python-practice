n=input('enter the string=')
s1=''
for i in n.split():
    s=i[::-1]
    s1=s1+s+' '
print(s1)    
