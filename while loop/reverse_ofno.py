num=int(input('enter the number'))
tmp=num
#num=str(num)
#reverse_digits=num[::-1]
reverse_digit=0
while num:
    digit=num%10
    reverse_digit=reverse_digit*10+digit
    num//=10

print(f'number{tmp},reverse digits{reverse_digit}')
