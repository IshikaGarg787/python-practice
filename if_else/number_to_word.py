a=int(input('enter no'))
m=a
n=a
f=0
while a>0:
    b=a%10
    f=f+1
    a=a//10
if f == 3:
    c=m//100
    if c==1:
        print('one hundred', end=' ')
    elif c==2:
        print('two hundred', end=' ')
    elif c==3:
        print('three hundred', end=' ')
    elif c==4:
        print('four hundred', end=' ')
    elif c==5:
        print('five hundred', end=' ')
    elif c==6:
        print('six hundred', end=' ')
    elif c==7:
        print('seven hundred', end=' ')
    elif c==8:
        print('eight hundred', end=' ')
    elif c==9:
        print("nine hundred", end=' ')
    c=m//10
    d=c%10
    if d==2:
        print("twenty", end=' ')
    elif d==3:
        print("thirty", end=' ')
    elif d==4:
        print("fourty", end=' ')
    elif d==5:
        print('fifty', end=' ')
    elif d==6:
        print('sixty', end=' ')
    elif d==7:
        print("seventy", end=' ')
    elif d==8:
        print('eighty', end=' ')
    elif d==9:
        print('ninety', end=' ')
    c=n%10
    if c==1:
        print("one", end=' ')
    elif c==2:
        print("two", end=' ')
    elif c==3:
        print("three", end=' ')
    elif c==4:
        print("four", end=' ')
    elif c==5:
        print("five", end=' ')
    elif c==6:
        print("six", end=' ')
    elif c==7:
        print("seven", end=' ')
    elif c==8:
        print("eight", end=' ')
    elif c==9:
        print("nine", end=' ')
if f==2:
    c=m//10
    d=c%10
    if d==2:
        print("twenty", end=' ')
    elif d==3:
        print("thirty", end=' ')
    elif d==4:
        print("fourty", end=' ')
    elif d==5:
        print('fifty', end=' ')
    elif d==6:
        print('sixty', end=' ')
    elif d==7:
        print("seventy", end=' ')
    elif d==8:
        print('eighty', end=' ')
    elif d==9:
        print('ninety', end=' ')
    c=n%10
    if c==1:
        print("one", end=' ')
    elif c==2:
        print("two", end=' ')
    elif c==3:
        print("three", end=' ')
    elif c==4:
        print("four", end=' ')
    elif c==5:
        print("five", end=' ')
    elif c==6:
        print("six", end=' ')
    elif c==7:
        print("seven", end=' ')
    elif c==8:
        print("eight", end=' ')
    elif c==9:
        print("nine", end=' ')
if f==1:
    if n==1:
        print("one")
    elif n==2:
        print("two")
    elif n==3:
        print("three")
    elif n==4:
        print("four")
    elif n==5:
        print("five")
    elif n==6:
        print("six")
    elif n==7:
        print("seven")
    elif n==8:
        print("eight")
    elif n==9:
        print("nine")
    elif n==10:
        print("ten")
if(n>10 or n<20):
    if(n==11):
        print("eleven")
    elif(n==12):
        print("twelve")
    elif(n==13):
        print("thirteen")
    elif(n==14):
        print("fourteen")
    elif(n==15):
        print("fifteen")
    elif(n==16):
        print("sixteen")
    elif(n==17):
        print("seventeen")
    elif(n==18):
        print("eighteen")
    elif(n==19):
        print("nineteen")
