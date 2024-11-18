# bad_code.py

import math,sys  # Multiple imports on one line

def calculate_area(radius): 
    if radius <= 0: print("Radius must be positive!")  # Inline if statement
    return math.pi*radius**2

def print_area(radius):
    area=calculate_area(radius)  # Missing spaces around assignment operator
    print(f"The area of the circle with radius {radius} is {area}") # Inconsistent indentation

for i in range(5): print_area(i+1) # Inline for loop, should be split onto separate lines
