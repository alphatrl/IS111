# Created by Amos Tan for students to reference their lab work
# Q2

PI = 3.14
radius = float(input("Please enter radius : "))

# Area : pi * r^2
area = PI * (radius ** 2)

# Circumference: pi * 2(r)
circumference = PI * 2 * radius

print(f"Area of circle of radius {radius}cm is {area} sq cm")
print(f"Circumference of circle of radius {radius}cm is {circumference} cm")
