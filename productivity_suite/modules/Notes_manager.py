import json
from datetime import datetime

NOTES_FILE = "data/notes.json"

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