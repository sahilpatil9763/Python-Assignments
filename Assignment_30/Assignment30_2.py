"""
2: Write a Python program that displays the current date and time after every one minute.

Use the datetime module.

Expected output:
Current Date and Time: 25-07-2026 04:30:00 PM
"""

import schedule
import time
import datetime

Border = "-"*40

def Display():
    print(datetime.datetime.now())

def main():
    print(Border)
    print("Automation Script Started")
    print(Border)

    schedule.every(1).minute.do(Display)

    # Record the starting time
    start = time.time()

    while True:
        schedule.run_pending()
        time.sleep(1)

        # Stop after 5 minutes
        if time.time() - start >= 5 * 60:               
            break
    
    print(Border)
    print("End of Automation Script")
    print(Border)

if __name__ == "__main__":
    main()