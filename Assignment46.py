def computepay(h,r):
    if(h>40):
        return r*(40+1.5*(h-40))
    else:
        return r*h

hrs = input("Enter Hours:")
h=float(hrs)
rate = input("Enter Rates:")
r=float(rate)
p=computepay(h,r)
print("Pay",str(p))