import os
import zipfile
from datetime import datetime

DATA_DIR = "data"
BACKUP_DIR = "data/backups"

class BackupManager:
    def backup(self):
        name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
        path = os.path.join(BACKUP_DIR, name)
        with zipfile.ZipFile(path, "w") as z:
            for f in os.listdir(DATA_DIR):
                if f != "backups":
                    z.write(os.path.join(DATA_DIR, f))
        print("✅ Backup created")

    def restore(self):
        files = os.listdir(BACKUP_DIR)
        if not files:
            print("No backups available")
            return
        for i, f in enumerate(files):
            print(i + 1, f)
        ch = int(input("Choose backup: ")) - 1
        with zipfile.ZipFile(os.path.join(BACKUP_DIR, files[ch]), "r") as z:
            z.extractall(DATA_DIR)
        print("♻️ Restore completed")