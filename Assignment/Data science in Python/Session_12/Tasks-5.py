ipl_scores = [101, 98, 120, 77, 88]

even_scores = list(filter(lambda score: score % 2 == 0, ipl_scores))

print(even_scores)
