def format_price(price, currency='INR'):
    if currency == 'INR':
        return f"₹{price}"
    elif currency == 'USD':
        return f"${price}"
    else:
        return f"{price}"

# Examples
print(format_price(500))          # Output: ₹500
print(format_price(500, 'USD'))   # Output: $500

