"""
5: Schedule a task that executes every five minutes.

The task should write the current date and time into a file named:

Marvellous.txt
New entries should be appended without removing previous entries.

Example file contents:
Task executed at: 25-07-2026 04:30:00 PM
Task executed at: 25-07-2026 04:35:00 PM
Task executed at: 25-07-2026 04:40:00 PM
"""

import schedule
import time
import datetime

Border = "-"*40

def FileCreate():
    try:
        fObj = open("Marvellous.txt","a")
        print("File created successfully!")

        fObj.write(f"Task executed at : {datetime.datetime.now()}\n")
        fObj.close()

    except FileNotFoundError as fObj:
        print("File is not present in current directory")

def main():
    print(Border)
    print("Automation Script Started")
    print(Border)

    schedule.every(5).minutes.do(FileCreate)

    while True:
        schedule.run_pending()
        time.sleep(1)

    print(Border)
    print("End of Automation Script")
    print(Border)

if __name__ == "__main__":
    main()