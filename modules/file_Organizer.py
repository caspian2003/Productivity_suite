import os
import shutil

class FileOrganizer:
    def organize(self):
        path = input("Enter folder path: ")
        if not os.path.exists(path):
            print("Invalid path")
            return

        for file in os.listdir(path):
            full = os.path.join(path, file)
            if os.path.isfile(full):
                ext = file.split(".")[-1].upper()
                folder = os.path.join(path, ext)
                os.makedirs(folder, exist_ok=True)
                shutil.move(full, os.path.join(folder, file))
        print("📁 Files organized")