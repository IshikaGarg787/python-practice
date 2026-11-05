married=input('enter married status if true or false only=')
has_dependents=input('has dependencies (enter true or false)=')

if married=='true':
    print("married")
elif married=='false' and has_dependents=='true':
   print('head of household')
elif married=='false' and has_dependents=='false':
   print('single')
