def apply_coupon(price, coupon_code=None):
    if coupon_code == 'ZOMATO10':
        return price - (price * 0.10)
    else:
        return price

# Examples
print(apply_coupon(1000, 'ZOMATO10'))  # Output: 900.0
print(apply_coupon(1000))              # Output: 1000
