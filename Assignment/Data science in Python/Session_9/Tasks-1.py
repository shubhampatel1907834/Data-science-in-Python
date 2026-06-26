def calculate_final_price(price, discount_rate):
    final_price = price - (price * discount_rate / 100)
    return final_price

# Example
print(calculate_final_price(1000, 20))  # Output: 800.0

