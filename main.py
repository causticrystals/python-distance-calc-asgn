# Distance Calculator Assignment
import math
print("Welcome to the distance calculator!")

# Input
x1 = float(input("Enter x1 "))
y1 = float(input("Enter y1 "))
x2 = float(input("Enter x2 "))
y2 = float(input("Enter y2 "))

# Process
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Output
print(distance)
