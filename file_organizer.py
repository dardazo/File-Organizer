import os
import shutil

# Function to create folder if it doesn't exist
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Function to organize files based on file extension
def organize_files(directory):
    # Dictionary to define file types and their corresponding folders
    file_types = {
        'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.mov', '.avi'],
        'Music': ['.mp3', '.wav'],
        'Archives': ['.zip', '.tar', '.rar'],
        'Others': []
    }

    # Loop through files in the specified directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        file_ext = os.path.splitext(filename)[1].lower()

        # Check the file type and move to corresponding folder
        moved = False
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                folder_path = os.path.join(directory, folder)
                create_folder(folder_path)
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved {filename} to {folder}")
                moved = True
                break

        # If no match found, move to "Others"
        if not moved:
            folder_path = os.path.join(directory, 'Others')
            create_folder(folder_path)
            shutil.move(file_path, os.path.join(folder_path, filename))
            print(f"Moved {filename} to Others")

# Ask user for the directory to organize
directory_to_organize = input("Enter the path of the directory to organize: ")
organize_files(directory_to_organize)
