loan_amount=float(input('enter the amount='))

if loan_amount<50000:
    repayment_term=5 
elif 50000<loan_amount<100000:
    repayment_term=10 
elif  loan_amount>100000:
    repayment_term=15

annual_income=int(input('enter annual income='))

if annual_income<30000:
    repayment_term+=2

print("repayment term=",repayment_term,"years")  
