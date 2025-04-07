# Function 1: Computes the area of a rectangle
def rect_area(length, width):
    return length * width

# Function 2: Computes the surface area of a rectangular solid
def rect_surface_area(length, width, height):
    return 2 * (rect_area(length, width) + rect_area(length, height) + rect_area(width, height))

# Request user input for the dimensions of a rectangular solid
length = int(input("Enter the length of the object as an integer: "))
width = int(input("Enter the width of the object as an integer: "))
height = int(input("Enter the height of the object as an integer: "))

# Display dimensions
print("Length =", length, "Width =", width, "Height =", height)

# Compute and display total surface area
print("Total Surface Area =", rect_surface_area(length, width, height))

# Compute and display area of a rectangle (if needed)
print("Area of the rectangle:", rect_area(length, width))
