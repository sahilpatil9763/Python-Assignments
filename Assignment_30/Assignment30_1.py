"""
1: Write a Python program that prints:
Jay Ganesh... 
every two seconds.

Use:
schedule.every(2).seconds.do(...)

Expected output:
Jay Ganesh.…
Jay Ganesh...
Jay Ganesh.…
"""

import schedule
import time

def Display():
    print("Jay Ganesh...")

def main():
    schedule.every(2).seconds.do(Display)

    # Record the starting time
    start = time.time()

    while True:
        schedule.run_pending()
        time.sleep(1)

        # Stop after 20 seconds
        if time.time() - start >= 20:
            print("\nProgram Stopped\n")
            break

if __name__ == "__main__":
    main()