"""
7: Write a Python program that performs a file backup every hour.
The program should:
    1. Accept the source file path.
    2. Accept the destination directory path.
    3. Copy the source file to the destination directory.
    4. Add the current date and time to the backup filename.
    5. Write the backup operation details into:

backup_log.txt
Example backup filename:
Data_25_07_2026_16_30_00.txt

Example log entry:
Backup completed successfully at 25-07-2026 04:30:00 PM

Use the shutil module for file copying.
"""

import schedule
import shutil
import time
import os
from datetime import datetime

Border = "-" * 50

# Function to perform backup
def BackupFile(SourceFile, DestinationDir):
    try:
        # Get file name without extension
        FileName = os.path.basename(SourceFile)
        Name, Extension = os.path.splitext(FileName)

        # Current date and time
        CurrentTime = datetime.now()

        # Create new backup file name
        BackupName = CurrentTime.strftime(f"{Name}_%d_%m_%Y_%H_%M_%S{Extension}")

        # Destination path
        DestinationPath = os.path.join(DestinationDir, BackupName)

        # Copy file
        shutil.copy2(SourceFile, DestinationPath)

        # Write log
        with open("backup_log.txt", "a") as LogFile:
            LogFile.write(
                "Backup completed successfully at "
                + CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p")
                + "\n"
            )

        print("Backup Created :", BackupName)

    except Exception as e:
        print("Error :", e)


def main():

    print(Border)
    print("File Backup Automation Started")
    print(Border)

    SourceFile = input("Enter source file path : ")
    DestinationDir = input("Enter destination directory : ")

    # Schedule every hour
    schedule.every().hour.do(BackupFile, SourceFile, DestinationDir)

    # First backup immediately (optional)
    BackupFile(SourceFile, DestinationDir)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()