import math
n = float(input("Enter a number: "))
if n >= 0:
    s = math.sqrt(n)
    print("The square root of", (n),"is", (s))
else:
    print("invalid value.")


n = int(input("Enter a number: "))
import math
factorial = math.factorial(n)
print("The factorial of",(n)," is",
factorial)


a = float(input("Enter the length of one side : "))
b = float(input("Enter the length of the other side: "))
import math
hypotenuse = math.hypot(a, b)
print("The hypotenuse of the triangle is",(hypotenuse))


degree = float(input("Enter an angle:",))
import math
radians = math.radians(degree)
s = math.sin(radians)
c = math.cos(radians)
t= math.tan(radians)
print("Sin",(degree),"° =",(s))
print("Cos",(degree),"°=",(c))
print("Tan",(degree),"° =",(t))



n = float(input("Enter a number: "))
import math
l = math.log(n)
print("The natural logarithm of",(n),"is",(l))

