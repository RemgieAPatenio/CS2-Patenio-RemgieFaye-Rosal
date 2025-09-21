import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

x = x2 - x1
y = y2 - y1

squared_x = math.pow(x, 2)
squared_y = math.pow(y, 2)

sum = squared_x + squared_y
distance = math.sqrt(sum)
print(f"The distance between the two points is: {distance:.2f}")