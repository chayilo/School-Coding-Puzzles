import math as m

l = int(input("Length of side of square"))
r = int(input("Radius of circle"))
d = 2*r
areaOfCircle = m.pi * r**2

if d >= 1:
    areaOfSquare = l**2
    excessArea = areaOfSquare - areaOfCircle
    print(excessArea)
    
else:
    print("Diameter of circle is greater than or equal to the length of square.")
