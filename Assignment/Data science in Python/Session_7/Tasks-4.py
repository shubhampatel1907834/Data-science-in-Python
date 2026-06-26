# Enter your IPL fantasy team points
points = int(input("Enter your IPL fantasy team points: "))

if points > 500:
    if points > 800:
        print("Champion")
    else:
        print("Top Performer")
else:
    print("Keep Trying")
