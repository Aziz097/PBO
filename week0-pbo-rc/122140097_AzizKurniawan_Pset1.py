# Problem Set - 1
# For the first problem, we’re going back to the old good day C++ Problem.
# Given any `integer` input, a triangle must be printed with the corresponding height.


def print_triangle(height):
    for i in range(1, height + 1):
        
        for j in range(height - i): # Print spaces
            print(" ", end="")
        
        for k in range(2 * i - 1): # Print asterisks
            print("*", end="")

        print() # Move to the next line

height = int(input("Enter the height of triangle: "))
print_triangle(height)