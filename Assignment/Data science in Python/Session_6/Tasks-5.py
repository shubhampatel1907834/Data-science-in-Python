def get_unique_artists(spotify_playlist1, spotify_playlist2):
    return spotify_playlist1.union(spotify_playlist2)
    # or: return spotify_playlist1 | spotify_playlist2

playlist1 = {"Arijit Singh", "Shreya Ghoshal", "Atif Aslam"}
playlist2 = {"Atif Aslam", "Neha Kakkar", "Armaan Malik"}

unique_artists = get_unique_artists(playlist1, playlist2)

print("All Unique Artists:")
print(unique_artists)
