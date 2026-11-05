destination=input("enter destination ,international or domestic only=")

if destination=='international':
    fee=30
elif destination=='domestic':
    fee=0

weight=float(input('enter the weight='))

if weight>10:
   fee=fee+((weight-10)*5)

     
    
print('shipping fee=',fee)
