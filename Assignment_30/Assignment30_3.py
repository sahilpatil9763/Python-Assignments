"""
3: Write a program that schedules a function to print.

Coding Kar..!

every 30 minutes
"""

import schedule
import time

Border = "-"*40

def Display():
    print("Coding Kar..!")

def main():
    print(Border)
    print("Automation Script Started")
    print(Border)

    schedule.every(30).minute.do(Display)

    start = time.time()

    while True:
        schedule.run_pending()
        time.sleep(1)

        # Stop after 1 hour
        if time.time() - start >= 60 * 60:               
            break

    print(Border)
    print("End of Automation Script")
    print(Border)

if __name__ == "__main__":
    main()