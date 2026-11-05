ls=[1,2,3,4,5,3,'hello',3,3]
val=3
for i in ls:
    if i==val:
       ls.remove(val)
#ls.remove(3)
print(ls)
