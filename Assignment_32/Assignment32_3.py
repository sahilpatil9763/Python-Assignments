"""
3: Write a program that reads and displays the contents of a specified text file every minute.
Handle the following conditions:
• File does not exist
• File is empty
• Permission is denied
• File cannot be opened
"""

import os
import schedule
import time

Border = "-" * 50

def ReadFile(FileName):

    print(Border)

    try:
        File = open(FileName, "r")

        Data = File.read()

        if len(Data) == 0:
            print("File is empty.")
        else:
            print("Contents of file:\n")
            print(Data)

        File.close()

    except FileNotFoundError:
        print("File does not exist.")

    except PermissionError:
        print("Permission denied.")

    except OSError:
        print("File cannot be opened.")

    print(Border)


def main():

    print(Border)
    print("Automation Script Started")
    print(Border)

    FileName = input("Enter File Path : ").strip()

    # Read file every minute
    schedule.every(1).minutes.do(ReadFile, FileName)

    # Read immediately
    ReadFile(FileName)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()