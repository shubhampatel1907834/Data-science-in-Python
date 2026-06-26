steps = [6500, 8200, 9800, 10500, 12000, 9000, 11000]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

i = 0

while i < len(steps):
    if steps[i] > 10000:
        print("First day crossing 10,000 steps:", days[i])
        break
    i += 1
