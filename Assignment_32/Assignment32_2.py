"""
2: Write a Python program that monitors the size of a specified file every 30 seconds.
Write the following details into:
FileSizeLog.txt
• File path
• File size in bytes
• Date and time
Handle the situation where the file does not exist.
"""

import sys
import os
import schedule
import time
import datetime

Border = "-" * 50

def MonitorFile(FileName):

    LogFile = open("FileSizeLog.txt", "a")

    LogFile.write(Border + "\n")

    if os.path.exists(FileName):

        Size = os.path.getsize(FileName)

        LogFile.write("File Path : " + FileName + "\n")
        LogFile.write("File Size : " + str(Size) + " Bytes\n")
        LogFile.write("Date and Time : " + datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

        print("File size recorded successfully.")

    else:

        LogFile.write("File Path : " + FileName + "\n")
        LogFile.write("Status : File does not exist\n")
        LogFile.write("Date and Time : " + datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

        print("File does not exist.")

        sys.exit()        

    LogFile.write(Border + "\n\n")
    LogFile.close()


def main():

    print(Border)
    print("Automation Script Started")
    print(Border)

    FileName = input("Enter File Path : ").strip()

    # Check every 30 seconds
    schedule.every(30).seconds.do(MonitorFile, FileName)

    # Check immediately
    MonitorFile(FileName)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()