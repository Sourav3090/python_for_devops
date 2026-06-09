#  Calculate area of a triangle 
# Input: base = 10, height = 6 
# Output: Area = ?.
def triangle_area(base, height):
    area = (1/2) * base * height
    return area

base = 10
height = 6

result = triangle_area(base, height)


print("Area =", result)



# . Calculate perimeter of a square 
# Input: side = 9 
# Output: Perimeter = ? 
def perimeter_square(side):
    perimeter = 4 * side
    return perimeter

side = 9

result = perimeter_square(side)

print("Perimeter =", result)



#  Calculate diameter of a circle 
# Input: radius = 14 
# Output: Diameter = ? 

def diameter_circle(radius):
    diameter = 2 * radius
    return diameter

radius = 14

result = diameter_circle(radius)

print("Diameter =", result)



#  Calculate volume of a cube 
# Input: side = 5 
# Output: Volume = ? 
def cube_volume(side):
    volume = side*side*side
    return volume

side = 5

result = cube_volume(side)

print("Volume =", result)


# . Calculate surface area of a cuboid 
# Input: l = 4, b = 3, h = 2 
# Output: Surface Area = ? 
def surface_area_cuboid(l, b, h):
    surface_area = 2 * (l * b + b * h + l * h)
    return surface_area

l = 4
b = 3
h = 2

result = surface_area_cuboid(l, b, h)

print("Surface Area =", result)

# Square of sum: (x + y)² 
# Input: x = 5, y = 7 
# Output: ?
# function to calculate square of sum
def square_of_sum(x, y):
    result = (x + y) ** 2
    return result

x = 5
y = 7

output = square_of_sum(x, y)

print("Output:", output)


# Simplify expression: x² - 4x + 4 
# Input: x = 3 
# Output: ? 

n=7
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")