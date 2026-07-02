def safe_divide_for_zomato(bill_amount, number_of_people):
    try:
        result = bill_amount / number_of_people

    except ZeroDivisionError:
        print("Error: Number of people cannot be zero.")

    else:
        print("Each person should pay: ₹", result)

    finally:
        print("Split calculation done")


# Examples
safe_divide_for_zomato(1200, 4)
print()

safe_divide_for_zomato(1200, 0)
