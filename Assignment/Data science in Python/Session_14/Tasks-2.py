# Reading playlist.txt and printing songs in uppercase

with open("playlist.txt", "r") as file:
    for song in file:
        print(song.strip().upper(
