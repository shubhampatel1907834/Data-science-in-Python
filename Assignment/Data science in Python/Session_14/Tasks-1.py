# Writing to playlist.txt

songs = [
    "Shape of You",
    "Blinding Lights",
    "Levitating",
    "Perfect",
    "Believer"
]

with open("playlist.txt", "w") as file:
    for song in songs:
        file.write(song + "\n")

print("playlist.txt created successfully.")
