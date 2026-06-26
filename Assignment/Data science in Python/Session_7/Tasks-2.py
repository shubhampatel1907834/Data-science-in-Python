# Enter your Zomato order amount
order_amount = float(input("Enter your Zomato order amount: "))

if order_amount > 300:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")
