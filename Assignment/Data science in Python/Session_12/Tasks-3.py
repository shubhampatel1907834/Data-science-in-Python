from functools import reduce

cart_prices = [499, 1299, 299, 799]

total = reduce(lambda x, y: x + y, cart_prices)

print(total)
