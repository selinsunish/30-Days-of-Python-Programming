import math
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
hypotenuse = math.hypot(side1, side2)
print(f"The length of the hypotenuse is: {hypotenuse}")
