match_id,team1,team2,winner
1,CSK,MI,CSK
2,RCB,KKR,KKR
3,GT,RR,GT

import csv

with open("ipl_matches.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Match Winners:")
    for row in reader:
        print(f"Match {row['match_id']}: {row['winner']}")
