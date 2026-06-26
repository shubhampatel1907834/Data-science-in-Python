# Enter your Flipkart cart total
cart_total = float(input("Enter your Flipkart cart total: "))

if cart_total > 2000:
    print("You get a 10% discount")
elif cart_total > 1000:
    print("You get a 5% discount")
else:
    print("No discount available")
