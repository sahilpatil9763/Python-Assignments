"""
5: Write a program that accepts a directory name from the user and
counts the number of files inside it every five minutes.

Write the result into:
DirectoryCountLog.txt

Each entry should contain:
• Directory path
• Number of files
• Date and time
"""

import os
import schedule
import time
import datetime

Border = "-" * 50

def CountFiles(DirectoryName):

    FileCount = 0

    for File in os.listdir(DirectoryName):

        Path = os.path.join(DirectoryName, File)

        if os.path.isfile(Path):
            FileCount = FileCount + 1

    LogFile = open("DirectoryCountLog.txt", "a")

    LogFile.write(Border + "\n")
    LogFile.write("Directory Path : " + DirectoryName + "\n")
    LogFile.write("Number of Files : " + str(FileCount) + "\n")
    LogFile.write("Date and Time : " + datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
    LogFile.write(Border + "\n\n")

    LogFile.close()

    print("Directory scanned successfully.")

def main():

    print(Border)
    print("Automation Script Started")
    print(Border)

    DirectoryName = input("Enter Directory Path : ").strip()

    if not os.path.isdir(DirectoryName):
        print("Invalid Directory")
        return

    # Scan every 5 minutes
    schedule.every(5).minutes.do(CountFiles, DirectoryName)

    # Scan immediately
    CountFiles(DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()