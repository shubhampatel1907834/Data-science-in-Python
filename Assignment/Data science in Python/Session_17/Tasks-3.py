from datetime import datetime

current_time = datetime.now()

formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")

print("Current Date and Time:", formatted_time)
