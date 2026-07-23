"""
5: Write a program that deletes all empty files from a specified directory every hour.
The program should:
• Scan the directory recursively
• Detect files whose size is zero bytes
• Delete the empty files
• Store deleted file paths in a log file
• Handle permission errors
Test the program only on a sample directory.
"""

import os
import schedule
import time
import sys
import datetime

Border = "-" * 50

def DirectoryScanner(DirectoryPath):

    CurrentTime = datetime.datetime.now()
    LogFileName = CurrentTime.strftime("Log_File_%d_%m_%Y_%H_%M_%S.txt")
    LogFileName = LogFileName.replace(" ","-")

    Ret = False

    Ret = os.path.exists(DirectoryPath)

    if(Ret == False):
        print("Automation Error : Their is no such directory with name ",DirectoryPath)
        return

    print("Log file gets created with name : ",LogFileName)

    File = open(LogFileName, "w")

    File.write(Border + "\n")
    File.write("Automation Script")
    File.write(Border + "\n\n")

    TotalFiles = 0
    EmptyFiles = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        for fname in FileName:
            TotalFiles = TotalFiles + 1

            fname = os.path.join(FolderName, fname)
            File.write(f"{fname} : {os.path.getsize(fname)} bytes\n")

            if os.path.getsize(fname) == 0:
                EmptyFiles = EmptyFiles + 1
                os.remove(fname)

    File.write(Border + "\n")
    File.write(f"Total files scanned : {TotalFiles}\n")
    File.write(f"Total empty files found and deleted  : {EmptyFiles}\n")

    File.write("Log file gets created : " + CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))

    File.close()

def main():

    print(Border)
    print("Automation Script Started\n")
    print(Border)

    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to delete all empty files from directory")

        else:
            schedule.every(1).hours.do(DirectoryScanner,sys.argv[1])
                # DirectoryScanner(sys.argv[1])

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid number of arguments")

    print(Border)
    print("Thank you for using the automation script")
    print(Border)

if __name__ == "__main__":
    main()