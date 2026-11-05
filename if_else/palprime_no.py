n = int(input('enter'))
s = str(n)
count=0
s1 = s[::-1]
if s == s1:
    for j in range(1,n+1):
            if (n%j==0):
                count=count+1
    if count==2:
        print('palprime no')
    else:
        print("not palprime no")
else:
    print('not palprime no')
