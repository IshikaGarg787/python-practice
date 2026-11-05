r=5
h=10
f=15
t=float(input("enter time:"))
vwtr=f*t
vtank=3.14*r**2*h
print("user given time:",t)
if vwtr==vtank:
    print("tank is full")
elif vwtr>vtank:
    print("tank is overflow")
    print("overflow volume",vwtr-vtank)
else:
    print("underflow condition")
    ht=vwtr/(3.14*r**2)
    hr=h-ht
    print("filled height",ht)
    print("remaining height",hr)
