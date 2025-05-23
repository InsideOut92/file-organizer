# 📂 File Organizer

![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A Python script that automatically sorts files into subfolders by type—perfect for keeping your working directories clean and organized!


## ✨ Features

- **Automatic sorting** by file type (Images, PDFs, Documents, etc.)
- **Robust logging** with rotation (no oversized log files)
- **Error tolerance:** Skips existing files and logs all issues
- **User-friendly:** Interactive terminal usage

## 🚀 Installation

1. Clone the repository:
   ```
   git clone https://github.com/InsideOut92/file-organizer.git
   ```
2. Change into the project directory:
   ```
   cd file-organizer
   ```

## 🛠️ Usage

1. Run the script:
   ```
   python file_organizer.py
   ```
2. Enter the path to the folder you want to organize when prompted:
   ```
   Enter the path to the folder you want to organize: /path/to/your/folder
   ```
3. **Sample output:**
   ```
   INFO - Moved: image.jpg to /path/to/your/folder/Images/image.jpg
   INFO - File organization completed.
   ```

## 📝 Logging

- Log files are stored in the `logs/organizer.log` directory.
- **Log rotation:** Automatically archives log files at 1 MB (up to 3 backups).
- **Format:** `TIMESTAMP - LEVEL - MESSAGE` (e.g., `2025-05-23 15:00:00 - INFO - Moved: document.pdf`).

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.