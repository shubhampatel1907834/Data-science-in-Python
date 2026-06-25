def total_cart_amount(prices):
    total = 0.0
    for price in prices:
        total += float(price)
    return total

cart_prices = ['199.99', '49', '350.75']
print("Total Cart Amount:", total_cart_amount(cart_prices))
