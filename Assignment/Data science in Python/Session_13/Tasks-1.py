def print_playlist_songs(songs):
    # Base case
    if not songs:
        return

    # Print the first song
    print(songs[0])

    # Recursive call with the remaining songs
    print_playlist_songs(songs[1:])

playlist = ["Shape of You", "Blinding Lights", "Levitating", "Senorita"]
print_playlist_songs(playlist)
