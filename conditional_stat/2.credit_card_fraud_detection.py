account_balance=float(input("enter account balance="))
transaction_amount=float(input('enter transaction amount='))
transaction_time=int(input('enter time in integer only 24hrs format(1-24)='))

if (account_balance*0.7)< transaction_amount:
 print("suspicious")
elif transaction_time>22 or transaction_time<6:
    print('suspicious')
else:
 print('safe')
