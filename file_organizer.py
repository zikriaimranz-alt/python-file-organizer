import os
import shutil

# ==========================================
# PYTHON FILE ORGANIZER
# ==========================================

# Ask user for folder path
folder = input("Enter the folder path: ")

# Check if folder exists
if not os.path.exists(folder):
    print("Folder does not exist!")
    exit()

# File categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".flac"],
    "Documents": [".pdf", ".docx", ".doc", ".txt"],
    "Excel": [".xlsx", ".xls", ".csv"],
    "Python": [".py"],
    "ZIP Files": [".zip", ".rar", ".7z"]
}

# Read all files in the folder
for file in os.listdir(folder):

    file_path = os.path.join(folder, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    extension = os.path.splitext(file)[1].lower()

    found = False

    # Find the correct category
    for category, extensions in categories.items():

        if extension in extensions:

            # Create category folder
            category_folder = os.path.join(folder, category)

            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

            # Move the file
            destination = os.path.join(category_folder, file)

            shutil.move(file_path, destination)

            print(file, "->", category)

            found = True
            break

    # If extension is not found
    if not found:

        other_folder = os.path.join(folder, "Others")

        if not os.path.exists(other_folder):
            os.makedirs(other_folder)

        destination = os.path.join(other_folder, file)

        shutil.move(file_path, destination)

        print(file, "-> Others")

print("\nFiles organized successfully!")