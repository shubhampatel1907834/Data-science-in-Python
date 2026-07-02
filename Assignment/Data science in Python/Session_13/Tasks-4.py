def format_number_short(n, units=["", "K", "M", "B", "T"], index=0):
    # Base case
    if n < 1000 or index == len(units) - 1:
        if index == 0:
            return str(int(n))
        return f"{n:.1f}{units[index]}"

    # Recursive call
    return format_number_short(n / 1000, units, index + 1)


# Examples
print(format_number_short(500))
print(format_number_short(1500))
print(format_number_short(1200000))
print(format_number_short(987654321))
