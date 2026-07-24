"""
Project : Duplicate File Removal Automation

Usage:
python DuplicateFileRemoval.py <DirectoryPath> <TimeInterval> <ReceiverEmail>
"""

import sys
import time
import os

from DirectoryScanner import ScanDirectory
from DuplicateFinder import FindDuplicate
from FileRemover import RemoveDuplicateFiles
from Logger import CreateLogFile
from EmailSender import SendEmail
from Schedular import StartScheduler


#----------------------------------------------------------
# Help
#----------------------------------------------------------

def Help():

    print("""
Duplicate File Removal Automation

Usage :
python DuplicateFileRemoval.py
<DirectoryPath>
<TimeInterval>
<ReceiverEmail>

Example :

python DuplicateFileRemoval.py
E:/Data 30 abc@gmail.com
""")


#----------------------------------------------------------
# Usage
#----------------------------------------------------------

def Usage():

    print("""
Command Format

python DuplicateFileRemoval.py
DirectoryPath
TimeInterval
ReceiverEmail
""")


#----------------------------------------------------------
# Validation
#----------------------------------------------------------

def ValidateArguments():

    if len(sys.argv) == 2:

        if sys.argv[1] == ["--help","--h","--H"]:
            Help()
            exit()

        elif sys.argv[1] == ["--usage","--u","--U"]:
            Usage()
            exit()

    if len(sys.argv) != 4:

        print("Invalid number of arguments")
        Usage()
        exit()

    Directory = sys.argv[1]

    if os.path.exists(Directory) == False:

        print("Directory does not exist.")
        exit()

    try:

        Interval = int(sys.argv[2])

        if Interval <= 0:
            raise Exception

    except:

        print("Invalid Time Interval")
        exit()


#----------------------------------------------------------
# Main Task
#----------------------------------------------------------

def DuplicateRemoval():

    Directory = sys.argv[1]

    ReceiverEmail = sys.argv[3]

    print("--------------------------------------")
    print("Scanning Started...")
    print("--------------------------------------")

    StartTime = time.strftime("%d/%m/%Y %I:%M:%S %p")

    FileList = ScanDirectory(Directory)

    TotalFiles = len(FileList)

    DuplicateData = FindDuplicate(Directory)

    DuplicateGroups = len(DuplicateData)

    DeletedFiles = RemoveDuplicateFiles(DuplicateData)

    EndTime = time.strftime("%d/%m/%Y %I:%M:%S %p")

    LogFile = CreateLogFile(
                    Directory,
                    TotalFiles,
                    DuplicateGroups,
                    DeletedFiles)

    #---------------------------------------------
    # Sender Details
    # Replace with your Gmail and App Password
    #---------------------------------------------

    SenderEmail = "yourgmail@gmail.com"

    AppPassword = "Your_App_Password"

    SendEmail(
        SenderEmail,
        AppPassword,
        ReceiverEmail,
        LogFile
    )

    print("--------------------------------------")
    print("Scanning Completed")
    print("Start :", StartTime)
    print("End   :", EndTime)
    print("Deleted :", len(DeletedFiles))
    print("--------------------------------------")


#----------------------------------------------------------
# Main
#----------------------------------------------------------

def main():

    ValidateArguments()

    Interval = int(sys.argv[2])

    # Run once immediately
    DuplicateRemoval()

    # Then run periodically
    StartScheduler(Interval, DuplicateRemoval)


if __name__ == "__main__":

    main()