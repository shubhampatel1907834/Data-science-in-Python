def print_long_team_names(teams):
    for team in teams:
        if len(team) <= 6:
            continue
        print(team)

ipl_teams = [
    "CSK",
    "MI",
    "RCB",
    "KKR",
    "Sunrisers",
    "Titans",
    "Royals",
    "Super Giants"
]

print_long_team_names(ipl_teams)
