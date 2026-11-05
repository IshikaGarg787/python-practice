purchase_amount=float(input('enter purchase amount='))

if purchase_amount>200:
    purchase_amount-=purchase_amount*0.15
elif 100<purchase_amount<200:
    purchase_amount-=purchase_amount*0.1

is_premium_member=input('enter true or false only=')

if is_premium_member=='true':
    
    purchase_amount-=purchase_amount*.05
    
print("total amount after discount=",purchase_amount)
