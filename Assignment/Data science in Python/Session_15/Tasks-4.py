def calculate_average_rating(total_rating, num_reviews):
    try:
        return total_rating / num_reviews
    except ZeroDivisionError:
        print("Error: Number of reviews cannot be zero.")
        return None
    finally:
        print("Thank you for using the calculator")


print(calculate_average_rating(500, 0))
