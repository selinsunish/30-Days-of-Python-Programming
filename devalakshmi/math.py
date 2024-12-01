import math
num = float(input("Enter a number to find its square root: "))

if num >= 0:
    square_root = math.sqrt(num)
    print(f"The square root of {num} is {square_root}")
else:
    print("Cannot calculate the square root of a negative number.")
