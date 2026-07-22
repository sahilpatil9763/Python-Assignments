"""
1: Write a program that accepts:
    • A message from the user
    • A time interval in seconds
Schedule the program to display the message repeatedly after the specified interval.

Example input:
Enter message: Jay Ganesh
Enter interval in seconds: 5

Expected output:
Jay Ganesh
every five seconds.

Validate that the interval is greater than zero.
"""

import schedule
import time

Border = "-" * 40

def Display(Message):
    print(Message)

def main():
    print(Border)
    print("Automation Script Started")
    print(Border)

    Message = input("Enter message : ")
    Interval = int(input("Enter interval in seconds : "))

    # Validate Interval
    if (Interval <= 0):
        print("Error : Interval must be greater than zero")
        return

    # Schedular
    schedule.every(Interval).seconds.do(Display, Message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()