amount=int(input("enter the amount:"))

amount=amount-100
a=amount//2000
amount=amount%2000
b=amount//500
amount=amount%500
c=amount//200
amount=amount%200
d=amount//100
amount=amount%100

print("number of two thousand notes:",a)
print("number of five hundred notes:",b)
print("number of two hundred notes:",c)
print("number of one hundred notes:",d+1)
