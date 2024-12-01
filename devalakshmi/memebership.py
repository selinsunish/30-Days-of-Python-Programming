#Membership operators
fruits = ['apple', 'banana', 'cherry']
if 'apple' in fruits:
    print("Apple is in the list.")
if 'orange' not in fruits:
    print("Orange is not in the list.")

# Identity Operators
x = [1, 2, 3]
y = x  
z = [1, 2, 3]  

if x is y:
    print("x and y refer to the same object.")

if x is not z:
    print("x and z do not refer to the same object.")
