"""
3: Write a program that scans a specified directory every minute.
The task should display:
• Directory name
• Number of files
• Number of subdirectories
• Date and time of scanning
Use the os module.

Example output:
Directory Scanned: E:/Data
Total Files: 15
Total Subdirectories: 4
Scan Time: 25-07-2026 04:30:00 PM
"""

import os
import schedule
import time
import datetime
import sys

Border = "-" * 50

def ScanDirectory(DirectoryName):
    FileCount = 0
    DirectoryCount = 0

    for File in os.listdir(DirectoryName):
        Path = os.path.join(DirectoryName, File)

        if os.path.isfile(Path):
            FileCount = FileCount + 1

        elif os.path.isdir(Path):
            DirectoryCount = DirectoryCount + 1

    print(Border)
    print("Directory Scanned : ",DirectoryName)
    print("Total Files : ",FileCount)
    print("Total Subdirectories : ",DirectoryCount)
    print("Scan Time : ", datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    print(Border)

def main():
    print(Border)
    print("Automation Script Started")
    print(Border)

    if len(sys.argv) != 2:
        print("Usage : python3 Assignment31_3.py <DirectoryPath>")
        return

    DirectoryName = sys.argv[1]

    if os.path.exists(DirectoryName) == False:
        print("Directory does not exist.")
        return

    # Schedular
    schedule.every(1).minute.do(ScanDirectory, DirectoryName)

    # Scan immediately
    ScanDirectory(DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()