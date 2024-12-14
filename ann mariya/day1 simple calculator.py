x=int(input("enter number"))
y=int(input("enter number"))
z=input("enter a operation")
if z=="sum":
    print("sum is",x+y)
if z=="difference":
    print("difference is",x-y)
if z=="product":
    print("product is",x*y)
if z=="division":
    print("quotient is",x/y)
if z=="remainder":
    print("remainder is",x%y)
else:
    print("invalid")