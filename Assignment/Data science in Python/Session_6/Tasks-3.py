food_prices = {
    "Pizza": 299,
    "Burger": 180,
    "Biryani": 250,
    "Pasta": 220,
    "Sandwich": 150
}

print("Food items costing more than ₹200:")
for item, price in food_prices.items():
    if price > 200:
        print(item, "₹", price)
