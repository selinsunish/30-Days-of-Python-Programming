import math


num = float(input("Enter a number to find its log (base e): "))

if num > 0:
    
    log_value = math.log(num)
    print(f"The natural logarithm (log base e) of {num} is {log_value}")
else:
    print("Error: Logarithm is undefined for non-positive numbers.")
