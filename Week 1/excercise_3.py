import math

def compute_area(r):
    return math.pi * r * r

r = float(input("What is the radius of the circle? "))
print(f"The area is: {compute_area(r)}")


