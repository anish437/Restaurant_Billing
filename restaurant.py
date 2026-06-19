menu={
    'chicken biryani': 250,
    'mutton biryani': 300,
    'veg biryani': 200,
    'fish biryani': 350,
    'paneer tikka': 150,
    'chicken tikka': 200,
}
print("Welcome to our nellore restaurant!")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item}: {price}")

order_total = 0
items_ordered = []

# Allow customer to order up to 5 items
for i in range(5):
    item = input("enter the item you want to order (or 'done' to finish): ")
    
    if item == "done":
        break
    
    if item in menu:
        quantity=int(input("how many plates do you want?"))
        item_cost = menu[item]*quantity
        order_total += item_cost
        items_ordered.append(item)
        print(f"Added {item} to your order. Total so far: {order_total}")
    else:
        print("sorry, we don't have that item on the menu.")

print(f"\nYour ordered items:")
for ordered_item in items_ordered:
    print(f"- {quantity} {ordered_item}")
print(f"Your total order amount is: {order_total}")