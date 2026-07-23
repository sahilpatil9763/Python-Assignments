"""
4: Write a program that copies all .txt files from one directory to another every ten minutes.
The program should:
• Accept source and destination directories
• Validate both directories
• Copy only . txt files
• Maintain a log of copied files
• Avoid terminating if one file cannot be copied
"""

import os
import shutil
import schedule
import time
import datetime

Border = "-" * 50

def CopyFiles(SourceDir, DestinationDir):

    LogFile = open("CopyLog.txt", "a")

    LogFile.write(Border + "\n")
    LogFile.write("Copy Time : " + datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

    for File in os.listdir(SourceDir):

        SourcePath = os.path.join(SourceDir, File)

        if os.path.isfile(SourcePath) and File.endswith(".txt"):

            DestinationPath = os.path.join(DestinationDir, File)

            try:
                shutil.copy2(SourcePath, DestinationPath)

                LogFile.write(File + " : Copied Successfully\n")
                print(File, "Copied Successfully")

            except Exception:
                LogFile.write(File + " : Copy Failed\n")
                print(File, "Copy Failed")

    LogFile.write(Border + "\n\n")
    LogFile.close()


def main():

    print(Border)
    print("Automation Script Started")
    print(Border)

    SourceDir = input("Enter Source Directory : ").strip()
    DestinationDir = input("Enter Destination Directory : ").strip()

    if not os.path.isdir(SourceDir):
        print("Invalid Source Directory")
        return

    if not os.path.isdir(DestinationDir):
        print("Invalid Destination Directory")
        return

    # Copy immediately
    CopyFiles(SourceDir, DestinationDir)

    # Copy every 10 minutes
    schedule.every(10).minutes.do(CopyFiles, SourceDir, DestinationDir)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()