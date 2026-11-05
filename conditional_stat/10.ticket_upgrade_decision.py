points=int(input('enter the points='))
is_overbooked=input('enter if flight is overbooked in true or false only=')
is_frequent_flyer=input('enter if is frequent flyer in true or false=')

if points>=1000:
 print('eligible')    
elif is_overbooked=='true':
    points>=800
elif  is_frequent_flyer=='true':
    points>=900
elif is_overbooked=='true' and is_frequent_flyer=='true':
    points>=700

print('eligible for upgrade')


if points<=1000 and is_overbooked=='false' and is_frequent_flyer=='false':
 print('not eligible for upgrade')
