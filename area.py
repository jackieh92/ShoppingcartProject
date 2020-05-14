def calc_area():
    length = int(input("Enter the length of the house"))
    width = int(input("Enter the width of the house"))
    area = length * width
    return area
    
from math import pi as p
def circle():
    radius = int(input("Please enter the radius of the circle"))
    circumference = radius * p * 2
    return circumference