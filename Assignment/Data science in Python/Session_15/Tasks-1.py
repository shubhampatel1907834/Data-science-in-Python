def get_song_duration_per_minute(total_duration, number_of_songs):
    try:
        average_duration = total_duration / number_of_songs
        print("Average song duration:", average_duration, "minutes")
    except ZeroDivisionError:
        print("Error: The number of songs cannot be zero.")
    finally:
        print("Calculation completed.")


# Example
get_song_duration_per_minute(120, 10)
get_song_duration_per_minute(120, 0)
