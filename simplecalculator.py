x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=input("Enter operation:")
if z=="Sum":
    print("Sum is ",x+y)
elif z=="Product":
    print("Product is",x*y)
elif z=="Division":
    print("Quotient is",x/y)
elif z=="Remainder":
    print("Remainder is ",x%y)
elif z=="Difference":
    print("Difference is ",x-y)
else:
    print("Invalid operator")