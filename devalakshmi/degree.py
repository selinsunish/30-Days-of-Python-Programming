import math

degree = float(input("Enter an angle in degrees: "))

radians = math.radians(degree)

sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)

print(f"Sin({degree}°) = {sin_value}")
print(f"Cos({degree}°) = {cos_value}")
print(f"Tan({degree}°) = {tan_value}")
