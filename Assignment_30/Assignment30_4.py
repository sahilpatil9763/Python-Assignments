"""
4: Create a task that executes every day at 9:00 AM and prints:

Namskar...

Use:
schedule.every().day.at("09:00").do(...)
"""

import schedule
import time

Border = "-"*40

def Display():
    print("Namaskar...")

def main():
    print(Border)
    print("Automation Script Started")
    print(Border)

    schedule.every().day.at("09:00").do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

    print(Border)
    print("End of Automation Script")
    print(Border)

if __name__ == "__main__":
    main()