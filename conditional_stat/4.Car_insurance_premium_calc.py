cage=int(input("enter the age of car="))

if cage<5:
  premium=500
elif 5<cage<10:
    premium=800
elif cage>10:
    premium=1200
    
oage=int(input("enter the age of car's owner="))
if oage<25:
  premiumcar=premium+premium*0.2

no_accidents=input("enter true or false=")

if no_accidents=="true":
  premium-=premium*0.1

print("premium=",premium)

