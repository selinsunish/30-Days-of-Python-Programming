#1st question
list = [1, 2, 3, 4, 5]
if 5 in list:
    print("5 is in the list.")
else:
    print("5 is not in the list.")

if 7 not in list:
    print("10 is not in the list.")

#2nd question
str1 = input("Enter the first str ")
str2 = input("Enter the second str: ")
final= str1 + " " + str2
print("Concatenated str:", final)

#3rd question
output = (3 + 6) * 6 - 9 / 3 + 20
print("Result is:", output)

#4th question
a = 5
b = 10
print("Is a less than b?", a < b)   
print("Is a greater than b?", a > b) 
print("Is a equal to b?", a == b)   
print("Is a not equal to b?", a != b)
print("Is a less than or equal to b?", a <= b)
print("Is a greater than or equal to b?", a >= b)

#5th question
km = int(input("Enter the distance in kilometers: "))
meters = km * 1000
print("(km) kilometers is equal to (meters) meters.")