import os
import shutil

def organize_files(directory_path):
    # Dictionary mapping file extensions to folder names
    file_types = {
        'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Scripts': ['.py', '.cpp', '.c', '.java'],
        'Zipped': ['.zip', '.rar']
    }

    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        
        # Skip directories
        if os.path.isdir(filepath):
            continue
            
        extension = os.path.splitext(filename)[1].lower()
        
        for folder, extensions in file_types.items():
            if extension in extensions:
                folder_path = os.path.join(directory_path, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(filepath, os.path.join(folder_path, filename))
                print(f"Moved {filename} to {folder}")

if __name__ == "__main__":
    path = input("Enter the directory path to organize: ")
    organize_files(path)
