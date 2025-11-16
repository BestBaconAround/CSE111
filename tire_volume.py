import math
from datetime import datetime

while True:
    try:
        tire_width = int(input("Enter a tire width in mm: "))
        break
    except ValueError:
        print("Please enter a number, not a letter.")

while True:
    try:
        tire_aspect = int(input("Enter a tire aspect ratio: "))
        break
    except ValueError:
        print("Please enter a number, not a letter.")

while True:
    try:
        wheel_size = int(input("Enter the wheel size in inches: "))
        break
    except ValueError:
        print("Please enter a number, not a letter.")

volume = (math.pi * tire_width**2 * tire_aspect * (tire_width * tire_aspect + 2540 * wheel_size)) / 10_000_000_000

today_date = datetime.now()

print(f"{today_date:%Y-%m-%d}")
print(f"Tire width: {tire_width}")
print(f"Tire aspect ratio: {tire_aspect}")
print(f"Wheel size: {wheel_size}")
print(f"Volume of the tire: {volume:.2f} liters")

with open("volumes.txt", "at") as file:
    file.write(
        f"{today_date:%Y-%m-%d}, "
        f"Tire width: {tire_width}, "
        f"Tire aspect ratio: {tire_aspect}, "
        f"Wheel size: {wheel_size}, "
        f"Volume: {volume:.2f} liters\n"
    )
