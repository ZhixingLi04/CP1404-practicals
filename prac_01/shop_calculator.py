"""
get items number

set total price = 0

for i in range(items_number):
    price = float(input("Price of items:"))
    total_price += price

add value checking

while items_number <=0:
    display "Invalid!"

if total_price > 100:
    discount = total_price * 0.1
    total_price -= discount

display all
"""

items_number = int(input("Please enter the number of items:"))
while items_number <=0:
    print("Invalid!")
    items_number = int(input("Please enter the number of items:"))

total_price = 0

for i in range(items_number):
    price = float(input("Price of items:"))
    total_price += price

if total_price > 100:
    discount = total_price * 0.1
    total_price -= discount

print(f"Total price for {items_number} items is ${total_price:.2f}")