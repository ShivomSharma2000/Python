# calculate area and circumference:
import math

def circum_status(radius):
    area = math.pi * (radius ** 2);
    circumference = 2 * math.pi * radius
    return area, circumference

area, circumference = circum_status(3);
print("Area: ", round(area, 2), " and circumference: ", round(circumference, 2))