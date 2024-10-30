import os
import shutil
from pathlib import Path

# Path to Desktop
path = Path.home() / "Desktop"

folders = []
names = []

def main():
    # Collect file extensions and names
    for name in os.listdir(path=path): 
        if '.' in name:
            extension = name.split(".")[-1]
            if extension not in folders:
                folders.append(extension)
                names.append(name)

    # Create folders based on file extensions
    for new_folder in folders:
        folder_path = path / new_folder  
        if not folder_path.exists():
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")

    # Move files to corresponding folders
    for name in names:
        source = path / name
        destination = path / name.split('.')[-1] / name
        try: 
            shutil.move(source, destination)
            print(f"Moved {name} to {destination}")
        except FileExistsError:
            print(f"File already exists at {destination}. Skipping {name}.")

    # Notify if no files were moved
    if len(names) == 0:
        print('Nothing was moved.')

# Run the script
if __name__ == "__main__":
    main()
