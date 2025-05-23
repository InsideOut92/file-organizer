"""
File Organizer
--------------
A python-script, which sorts files in a given directory, sorts them by type and moves them in subdirectories.
All actions are documentated in the log file.

Author: Patrick Scharf
Date:   2025-05-23
"""

import os
import shutil
import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'PDFs': ['.pdf'],
    'Documents': ['.docx', '.txt', '.pptx', '.xlsx', '.doc', '.odt'],
    'Spreadsheets': ['.xlsx','.xls', '.csv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Others': []
}

LOG_DIR = 'logs'
LOG_FILE = os.path.join(LOG_DIR, 'organizer.log')

def setup_logging():
    os.makedirs(LOG_DIR, exist_ok=True)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # rotating file handler (max. 1 MB each file, 3 backups)
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=3, encoding='utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # console handler for direct output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def get_file_category(filename: str) -> str:
    """
    Determines the category of a file based on its extension.
    """
    _, ext = os.path.splitext(filename)
    ext = ext.lower() # for case-insensitive comparison

    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category

    return 'Others'

def organize_files(source_folder: str) -> None:
    """
    Organizes files in the specified folder into subfolders based on their file types.
    """
    logger = logging.getLogger()

    try:
        with os.scandir(source_folder) as entries:
            for entry in entries:
                if not entry.is_file():
                    continue

                category = get_file_category(entry.name)
                target_dir = os.path.join(source_folder, category)

                # create target directory if it doesn't exist
                os.makedirs(target_dir, exist_ok=True)

                # create target file path and move the file
                target_path = os.path.join(target_dir, entry.name)

                # only move if the target file doesn't exist in the target directory
                if not os.path.exists(target_path):
                    shutil.move(entry.path, target_path)
                    logger.info(f"Moved: {entry.name} to {target_path}")
                else:
                    logger.warning(f"File already exists: {entry.name} in: {target_path}. Skipping move.")

    except Exception as e:
        error_item = entry.name if 'entry' in locals() else 'unknown file'
        logger.error(f"An error occured at {entry.name}: {str(e)}", exc_info=True)
        raise 

def main():
    setup_logging()
    print("Welcome to the File Organizer!")
    print("This program will help you organize your files into folders based on their types.")
    source_folder = input("Enter the path to the folder you want to organize: ").strip()
    if not os.path.isdir(source_folder):
        print("Error: The specified path is not valid. Please try again.")
        return
    
    organize_files(source_folder)
    logging.info("File organization completed.")
    print("File organization completed. Check the logs for details.")
    
if __name__ == "__main__":
    main()