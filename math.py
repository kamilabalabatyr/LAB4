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

if __name__ == "__main__":
    # Math operations
    degree = float(input("Input degree: "))
    print("Output radian:", degrees_to_radians(degree))
    
    height = float(input("Height of trapezoid: "))
    base1 = float(input("Base, first value: "))
    base2 = float(input("Base, second value: "))
    print("Trapezoid area:", trapezoid_area(height, base1, base2))
    
    sides = int(input("Input number of sides: "))
    length = float(input("Input the length of a side: "))
    print("Polygon area:", polygon_area(sides, length))
    
    base = float(input("Length of base of parallelogram: "))
    height = float(input("Height of parallelogram: "))
    print("Parallelogram area:", parallelogram_area(base, height))

