age=int(input("enter age="))
ticket_price=float(input("enter ticket price="))
if age<12:
    ticket_price-=ticket_price*0.5
    
elif age>=60:
        ticket_price-=ticket_price*0.3
    
    
is_3D_movie=input("enter true or false=")
if is_3D_movie=='true':
    ticket_price=ticket_price+5
    
    print('total price=',ticket_price)
