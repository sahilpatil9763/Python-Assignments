"""
4: Write a program that creates a new log file after every ten minutes.

The filename should contain the current date and time.

Example:
MarvellousLog_25_07_2026_16_30_00.txt

The file should contain:
Log file created successfully.
Creation Time: 25-07-2026 04:30:00 PM
"""

import schedule
import time
import datetime

Border = "-" * 50

def CreateLog():

    CurrentTime = datetime.datetime.now()

    FileName = CurrentTime.strftime("MarvellousLog_%d_%m_%Y_%H_%M_%S.txt")

    File = open(FileName, "w")

    File.write("Log file created successfully.\n")
    File.write("Creation Time : ")
    File.write(CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))

    File.close()

    print(FileName, "created successfully.")

def main():
    print(Border)
    print("Automation Script Started")
    print(Border)

    # Create log file in every 10 minutes
    schedule.every(10).minutes.do(CreateLog)

    # Create first logg immediately
    CreateLog()

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()