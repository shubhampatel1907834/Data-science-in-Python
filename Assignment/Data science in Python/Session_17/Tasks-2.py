import os

folder_name = "MyDownloads"

os.makedirs(folder_name, exist_ok=True)

print("Folder created successfully.")
print("Absolute Path:", os.path.abspath(folder_name))
