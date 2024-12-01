percentage = float(input("Enter the percentage: "))

if percentage > 90:
    grade = 'A'
elif 80 < percentage <= 90:
    grade = 'B'
elif 60 <= percentage <=80:
    grade = 'C'
else:
    grade = 'D'

print(f"The grade is: {grade}")
