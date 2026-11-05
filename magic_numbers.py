n=int(input('enter the four digit number='))
kaprekar_num=6174
steps=0
while n!=kaprekar_num:
    num_str=f"{n:04d}"
    asc=int(''.join(sorted(num_str)))
    des=int(''.join(sorted(num_str,reverse=True)))
    n=des-asc
    steps+=1
print(f'threre are {steps} steps(s) to reach kaprekar number')

   

    
   


