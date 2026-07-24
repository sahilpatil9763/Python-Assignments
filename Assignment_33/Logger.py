"""
Module Name : Logger.py

Description :
Creates a log file containing all information
about duplicate file removal.
"""

import os
import time


#----------------------------------------------------------
# Function Name : CreateLogFile
# Description   : Creates log file
#----------------------------------------------------------

def CreateLogFile(DirectoryName,
                  TotalFiles,
                  DuplicateGroups,
                  DeletedFiles):

    # Create Marvellous directory
    LogDirectory = "Marvellous"

    if os.path.exists(LogDirectory) == False:
        os.mkdir(LogDirectory)

    # Generate timestamp
    TimeStamp = time.strftime("%d_%m_%Y_%H_%M_%S")

    LogFileName = "DuplicateRemovalLog_" + TimeStamp + ".log"

    LogPath = os.path.join(LogDirectory, LogFileName)

    fd = open(LogPath, "w")

    fd.write("*" * 60 + "\n")
    fd.write("         Duplicate File Removal Log\n")
    fd.write("*" * 60 + "\n\n")

    fd.write("Scanning Time : ")
    fd.write(time.strftime("%d/%m/%Y %I:%M:%S %p"))
    fd.write("\n\n")

    fd.write("Directory Scanned : ")
    fd.write(DirectoryName)
    fd.write("\n\n")

    fd.write("Total Files Scanned : ")
    fd.write(str(TotalFiles))
    fd.write("\n")

    fd.write("Duplicate Groups : ")
    fd.write(str(DuplicateGroups))
    fd.write("\n")

    fd.write("Deleted Files : ")
    fd.write(str(len(DeletedFiles)))
    fd.write("\n\n")

    fd.write("-" * 60)
    fd.write("\n")

    if len(DeletedFiles) == 0:
        fd.write("No duplicate files found.\n")
    else:

        fd.write("Deleted File List\n\n")

        Count = 1

        for File in DeletedFiles:

            fd.write(str(Count))
            fd.write(". ")
            fd.write(File)
            fd.write("\n")

            Count = Count + 1

    fd.write("\n")
    fd.write("-" * 60)
    fd.write("\n")

    fd.write("Log Generated Successfully\n")

    fd.close()

    return LogPath