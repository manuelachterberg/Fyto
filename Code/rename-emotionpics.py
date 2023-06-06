import os
import shutil
import tkinter as tk
from tkinter import filedialog


import os
import shutil
import tkinter as tk
from tkinter import filedialog


def select_destination_folder():
    root = tk.Tk()
    root.withdraw()

    # Prompt the user to select a destination folder
    destination_folder = filedialog.askdirectory(title="Select Destination Folder")
    return destination_folder


def rename_and_move_png_files(source_folder, destination_folder):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    # Check if the destination folder exists, otherwise create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get a list of PNG files in the source folder
    png_files = [f for f in os.listdir(source_folder) if f.endswith('.png')]

    if not png_files:
        print("No PNG files found in the source folder.")
        return

    # Sort the PNG files alphabetically
    png_files.sort()

    # Rename and move the PNG files
    for index, file_name in enumerate(png_files):
        # Generate the new file name
        new_file_name = f"frame{index}.png"

        # Construct the paths for the source and destination files
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, new_file_name)

        # Move the file to the destination folder with the new name
        shutil.move(source_path, destination_path)

        print(f"Moved '{file_name}' to '{new_file_name}'")


def delete_files_in_folder(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    # Get a list of files in the folder
    files = os.listdir(folder_path)

    if not files:
        print(f"No files found in the folder '{folder_path}'.")
        return

    # Delete each file in the folder
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted file '{file_name}' in '{folder_path}'.")


# Example usage
source_folder = "newEmotions"  # Path to the folder with PNG files

# Prompt the user to select a destination folder
print("Please select the destination folder")
destination_folder = select_destination_folder()

delete_files_in_folder(destination_folder)
rename_and_move_png_files(source_folder, destination_folder)