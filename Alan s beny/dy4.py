a = int(input("Enter the first number: "))
b= int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a >= b:
    if a >= c:
        print("largest =",a)
    else:
        print("largest =",c)
else:
    if b >= c:
        print("largest =",b)
    else:
        print("largest =", c)
        

x = int(input("Enter a number: "))

if x % 2 == 0:
    print(x," is divisible by 2.")
else:
    print(x," is not divisible by 2.")
    

percentage = float(input("Enter your percentage: "))

if percentage > 90:
    print("Your grade is:A")
elif percentage > 80 and percentage <= 90:
    print("Your grade is:B")
elif percentage >= 60 and percentage <= 80:
    print("Your grade is:C")
else:
    print("Your grade is:D")
