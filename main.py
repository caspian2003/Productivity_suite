import os
import json
import time
import shutil
import zipfile
from datetime import datetime

DATA_DIR = "data"
BACKUP_DIR = "data/backups"
NOTES_FILE = "data/notes.json"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(BACKUP_DIR, exist_ok=True)


# ===================== CALCULATOR =====================
class Calculator:
    def run(self):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
            op = input("Choose operation: ")

            if op == "1":
                print("Result:", a + b)
            elif op == "2":
                print("Result:", a - b)
            elif op == "3":
                print("Result:", a * b)
            elif op == "4":
                print("Result:", a / b if b != 0 else "Cannot divide by zero")
            else:
                print("Invalid operation")
        except ValueError:
            print("Invalid number input")


# ===================== NOTES MANAGER =====================
class NotesManager:
    def __init__(self):
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with open(NOTES_FILE, "r") as f:
                self.notes = json.load(f)
        except FileNotFoundError:
            self.notes = []

    def save_notes(self):
        with open(NOTES_FILE, "w") as f:
            json.dump(self.notes, f, indent=2)

    def add_note(self):
        title = input("Title: ")
        content = input("Content: ")
        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "content": content,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.notes.append(note)
        self.save_notes()
        print("✅ Note added")

    def view_notes(self):
        if not self.notes:
            print("No notes found")
        for n in self.notes:
            print(f"\nID: {n['id']}\nTitle: {n['title']}\n{n['content']}")

    def run(self):
        while True:
            print("\n1. Add Note\n2. View Notes\n3. Back")
            ch = input("Choice: ")
            if ch == "1":
                self.add_note()
            elif ch == "2":
                self.view_notes()
            elif ch == "3":
                break
            else:
                print("Invalid choice")


# ===================== TIMER =====================
class Timer:
    def countdown(self):
        try:
            seconds = int(input("Enter seconds: "))
            while seconds:
                print(f"Time left: {seconds}s")
                time.sleep(1)
                seconds -= 1
            print("⏰ Time's up!")
        except ValueError:
            print("Invalid input")


# ===================== STOPWATCH =====================
class Stopwatch:
    def run(self):
        input("Press Enter to start stopwatch")
        start = time.time()
        input("Press Enter to stop")
        end = time.time()
        print(f"Elapsed Time: {round(end - start, 2)} seconds")


# ===================== FILE ORGANIZER =====================
class FileOrganizer:
    def organize(self):
        path = input("Enter folder path: ")
        if not os.path.exists(path):
            print("Invalid path")
            return

        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                ext = file.split(".")[-1]
                folder = os.path.join(path, ext.upper())
                os.makedirs(folder, exist_ok=True)
                shutil.move(os.path.join(path, file), os.path.join(folder, file))
        print("📁 Files organized")


# ===================== UNIT CONVERTER =====================
class UnitConverter:
    def run(self):
        print("1. cm to m\n2. kg to g\n3. C to F")
        ch = input("Choice: ")
        try:
            val = float(input("Enter value: "))
            if ch == "1":
                print("Result:", val / 100, "m")
            elif ch == "2":
                print("Result:", val * 1000, "g")
            elif ch == "3":
                print("Result:", (val * 9/5) + 32, "F")
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid number")


# ===================== BACKUP & RESTORE =====================
class BackupManager:
    def backup(self):
        name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
        path = os.path.join(BACKUP_DIR, name)
        with zipfile.ZipFile(path, "w") as z:
            for file in os.listdir(DATA_DIR):
                if file != "backups":
                    z.write(os.path.join(DATA_DIR, file))
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


# ===================== MAIN MENU =====================
def main():
    calc = Calculator()
    notes = NotesManager()
    timer = Timer()
    watch = Stopwatch()
    organizer = FileOrganizer()
    converter = UnitConverter()
    backup = BackupManager()

    while True:
        print("\n==== PERSONAL PRODUCTIVITY SUITE ====")
        print("1. Calculator")
        print("2. Notes Manager")
        print("3. Timer")
        print("4. Stopwatch")
        print("5. File Organizer")
        print("6. Unit Converter")
        print("7. Backup")
        print("8. Restore")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            calc.run()
        elif choice == "2":
            notes.run()
        elif choice == "3":
            timer.countdown()
        elif choice == "4":
            watch.run()
        elif choice == "5":
            organizer.organize()
        elif choice == "6":
            converter.run()
        elif choice == "7":
            backup.backup()
        elif choice == "8":
            backup.restore()
        elif choice == "9":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()