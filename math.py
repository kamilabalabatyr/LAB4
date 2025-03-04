import math

# Convert degrees to radians
def degrees_to_radians(degree):
    return math.radians(degree)

# Calculate the area of a trapezoid
def trapezoid_area(height, base1, base2):
    return ((base1 + base2) / 2) * height

# Calculate the area of a regular polygon
def polygon_area(sides, length):
    return (sides * (length ** 2)) / (4 * math.tan(math.pi / sides))

# Calculate the area of a parallelogram
def parallelogram_area(base, height):
    return base * height

