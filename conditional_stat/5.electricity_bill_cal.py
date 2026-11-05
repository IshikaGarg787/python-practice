units = float(input("Enter the units consumed: "))

if units <= 100:
    cost = units * 0.50
elif units <= 200:
    cost = units * 0.75
else:
    cost = units * 1.20

if cost >= 300:
    cost += cost * 0.15  

print("Total bill = ₹",cost)
    
    
