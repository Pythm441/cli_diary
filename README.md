# 📝 Personal Diary CLI App

A simple command-line diary application built in Python to help you record your daily thoughts and emotions in a structured and organized way.

Each diary entry is saved in a folder structure based on the **year/month/day**, like:

Diary/
├── 2025/
│ └── 07/
│ └── 06.txt


## 🚀 Features

- Create a new diary entry for the current day.
- Automatically creates folders for year and month if they don’t exist.
- View past entries by entering a specific date (YYYY-MM-DD).
- Entries are saved in plain `.txt` format for simplicity and easy access.

## 📂 Folder Structure

Diary/
├── 2025/
│ ├── 01/
│ │ └── 01.txt
│ └── 07/
│ └── 06.txt


## 🛠 How to Run

1. Make sure you have Python installed (version 3+).
2. Clone or download the repository.
3. Open a terminal in the project folder.
4. Run the program:

```bash
python3 diary.py
