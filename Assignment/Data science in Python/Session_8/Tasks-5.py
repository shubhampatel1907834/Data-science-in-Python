# List of item prices in a Flipkart cart
item_prices = [450, 800, 0, 600, 300, 900, 250]

total = 0

for price in item_prices:
    # Skip out-of-stock items
    if price == 0:
        continue

    total += price

    # Stop if total crosses ₹2000
    if total > 2000:
        break

print("Final Total: ₹", total)
