num = int(input("Enter a number: "))

sum_of_digits = 0

for digit in str(num):
    sum_of_digits += int(digit)  

print("Sum of the digits:", sum_of_digits)
