try:
    total_amount = float(input("Enter total cart amount: ₹"))
    item_count = int(input("Enter number of items: "))

    price_per_item = total_amount / item_count
    print("Price per item: ₹", price_per_item)

except ZeroDivisionError:
    print("Error: Item count cannot be zero. Please enter at least one item.")

except ValueError:
    print("Error: Please enter valid numeric values.")
