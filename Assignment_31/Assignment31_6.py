"""
6: Write a program that schedules the following messages:

• Monday at 9:00 AM: Start your weekly goals
• Wednesday at 5:00 PM: Review your weekly progress
• Friday at 6:00 PM: Weekly work completed

Use:
schedule.every().monday.at(...)
schedule.every().wednesday.at(...)
schedule.every().friday.at(...)
"""

import schedule
import time
import datetime

Border = "-" * 50

def MondayTask():
    print("Start your weekly goals")

def WednesdayTask():
    print("Review your weekly progress")

def FridayTask():
    print("Weekly work completed")


def main():

    print(Border)
    print("Automation Script Started")
    print(Border)

    # Schedule the tasks
    schedule.every().monday.at("09:00").do(MondayTask)
    schedule.every().wednesday.at("17:00").do(WednesdayTask)
    schedule.every().friday.at("18:00").do(FridayTask)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()