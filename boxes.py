import math

items = int(input("Enter the number of items: "))
boxes = int(input("Enter the number of items per box: "))

total = math.ceil(items / boxes)

print(f"For {items} items, packing {boxes} items in each box, you will need {total} boxes")