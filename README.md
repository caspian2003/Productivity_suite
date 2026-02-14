# Personal Productivity Suite

## Project Overview
The Personal Productivity Suite is a command-line based Python application
developed as part of an internship project. It integrates multiple productivity
tools into a single, modular system using object-oriented programming and
file-handling techniques.

The application focuses on clean architecture, data persistence, and user-friendly
command-line interaction.

---

## Features
- Calculator (basic arithmetic operations)
- Notes Manager with persistent storage (JSON)
- Timer and Stopwatch
- File Organizer (organizes files by extension)
- Unit Converter (length, weight, temperature)
- Backup and Restore functionality
- Error handling for all user inputs

---

## Architecture
The project follows a modular, object-oriented architecture.

- `main.py` acts as the entry point and controller.
- Each tool is implemented as a separate module inside the `modules/` directory.
- Persistent data is stored in the `data/` directory using JSON and ZIP formats.
- The design follows separation of concerns for maintainability and scalability.

---

## Project Structure
productivity-suite/ ├── main.py ├── README.md ├── requirements.txt ├── modules/ │   ├── calculator.py │   ├── notes_manager.py │   ├── timer.py │   ├── file_organizer.py │   ├── unit_converter.py │   └── backup_manager.py ├── data/ │   ├── notes.json │   └── backups/ └── docs/ └── user_manual.md
Copy code

---

## Installation & Setup
1. Install Python 3.10 or higher
2. Clone this repository
3. Navigate to the project directory
4. Run the application:
   ```bash
   python main.py
Error Handling
All user inputs are validated using try-except blocks to prevent application crashes and improve the user experience.
Future Enhancements
Graphical User Interface (GUI)
Cloud-based data synchronization
Advanced data analytics.
