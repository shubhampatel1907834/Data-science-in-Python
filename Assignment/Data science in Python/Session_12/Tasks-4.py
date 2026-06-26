def format_followers(number):
    if number >= 1_000_000:
        return f"{number / 1_000_000:.1f}M"
    elif number >= 1_000:
        return f"{number / 1_000:.1f}K"
    else:
        return str(number)

followers = [950, 1500, 25000, 1200000]

formatted = list(map(format_followers, followers))

print(formatted)
