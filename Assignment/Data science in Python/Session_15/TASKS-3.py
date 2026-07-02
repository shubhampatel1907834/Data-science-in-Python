class NoOffersApplied(Exception):
    pass


try:
    total_spend = float(input("Enter total spend: ₹"))
    offers = int(input("Enter number of offers applied: "))

    if offers == 0:
        raise NoOffersApplied("No offers were applied. Cashback cannot be calculated.")

    average_cashback = total_spend / offers
    print("Average cashback per offer: ₹", average_cashback)

except NoOffersApplied as e:
    print("Custom Error:", e)

except ValueError:
    print("Please enter valid numbers.")
