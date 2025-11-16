from datetime import datetime

a = 1.556
b = round(a, 2)
print(b)


discount_rate = .1
tax_rate = .06
today = datetime.now()
dow = today.weekday()
subtotal = 0
quantity = 1
print(f"Today is {dow}")
while quantity != 0:
   quantity = int(input("Enter the quantiy: "))
   if quantity != 0:
    price = float(input("Enter the price: "))
    subtotal += quantity * price
print(f"Total order ${subtotal:.2f}")
discount = 0
if dow == 1 or dow == 2:
    if subtotal >= 50:
     discount = round(subtotal * discount_rate)
     print(f"Discount ${discount:.2f}")
    else:
       short = 50 - subtotal
       print(f"You can get a discount by ordering ${short:.2f} more.")
subtotal -= discount 
tax = subtotal * tax_rate
total = round(subtotal + tax)

print(f"Tax ${tax:.2f}")
print(f"Total Due ${total:.2f}")