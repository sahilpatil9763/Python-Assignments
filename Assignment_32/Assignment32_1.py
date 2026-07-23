"""
1: Write a program that creates a new text file every minute.
The filename should contain the current timestamp.

Example:
File_25_07_2026_16_30_00.txt

Write the following information into the file:
• Filename
• Creation date
• Creation time
"""

import schedule
import time
import datetime

Border = "-" * 50

def CreateFile():

    CurrentTime = datetime.datetime.now()

    FileName = CurrentTime.strftime("File_%d_%m_%Y_%H_%M_%S.txt")

    File = open(FileName, "w")

    File.write(Border + "\n")
    File.write("Filename : " + FileName + "\n")
    File.write("Creation date : " + CurrentTime.strftime("%d-%m-%Y") + "\n")
    File.write("Creation Time : " + CurrentTime.strftime("%I:%M:%S %p") + "\n")
    File.write(Border + "\n")

    File.close()

    print(FileName, "created successfully.")

def main():

    print(Border)
    print("Automation Script Started")
    print(Border)

    # Create file every minute
    schedule.every(1).minutes.do(CreateFile)

    # Create the first file immediately
    # CreateFile()

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()