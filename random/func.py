"""def add(first, second):
    result = first + second 
    return result

x = 3
y = 4
total = add(x, y)
print(total)

total = add(y, y)
print(total)"""

"""def get_positive_value(prompt_text):
    value = float(input(prompt_text))

    while value < 0:
        print("Sorry, the value cannot be a negative")
        value = float(input(prompt_text))
    return value

length = get_positive_value("What is the length of a rectangle? ")
width = get_positive_value("What is the width of the rectangle? ")

area = length * width

print(f"The area is {area}")"""

import math
def maths():
    radius = float(input("Enter the radius: "))
    height = float(input("Enter the height: "))
    volume = math.pi * radius**2 * height
    print(f"The volume {volume:.2f}")
maths()