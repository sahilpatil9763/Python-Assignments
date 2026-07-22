"""
6: Write a script that schedules the following tasks:

Print Lunch Time! every day at 1:00 PM.
Print Wrap up work every day at 6:00 PM.

Both tasks should be handled by separate functions.
"""

import schedule
import time

Border = "-"*40

def Lunch():
    print("Lunch Time!")

def WrapWork():
    print("Wrap up work")

def main():
    print(Border)
    print("Automation Script Started")
    print(Border)

    schedule.every().day.at("13:00").do(Lunch)
    schedule.every().day.at("18:00 PM").do(WrapWork)

    while True:
        schedule.run_pending()
        time.sleep(1)
        

    print(Border)
    print("End of Automation Script")
    print(Border)

if __name__ == "__main__":
    main()