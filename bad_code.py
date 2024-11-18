'''
filename: bad_code.py

'''


import math

def calculate_area(radius):
    '''
    calcualtes area from radius
    '''
    if radius <= 0: 
        print("Radius must be positive!")  # Inline if statement
    return math.pi*radius**2

def print_area(radius):
    '''
    prints area
    '''
    area = calculate_area(radius)  # Missing spaces around assignment operator
    print(f"The area of the circle with radius {radius} is {area}") # Inconsistent indentation

for i in range(5): 
    print_area(i+1) # Inline for loop, should be split onto separate line
