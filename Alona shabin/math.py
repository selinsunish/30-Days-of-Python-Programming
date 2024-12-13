import math
num = float(input("Enter a number "))
if num >= 0:
    square_root = math.sqrt(num)
    print(f"The square root of {num} is {square_root}")
else:
    print("invalid")
