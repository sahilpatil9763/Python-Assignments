"""
Module Name : DuplicateFinder.py

Description :
This module finds duplicate files by comparing
their MD5 checksum values.
"""

from DirectoryScanner import ScanDirectory
from CheckSum import CalculateChecksum


#----------------------------------------------------------
# Function Name : FindDuplicate
# Description   : Finds duplicate files
# Input         : Directory Path
# Output        : Dictionary containing duplicate files
#----------------------------------------------------------

def FindDuplicate(DirectoryName):

    # Get all files from the directory
    FileList = ScanDirectory(DirectoryName)

    DuplicateFiles = {}

    for File in FileList:

        Checksum = CalculateChecksum(File)

        if Checksum == None:
            continue

        if Checksum in DuplicateFiles:
            DuplicateFiles[Checksum].append(File)
        else:
            DuplicateFiles[Checksum] = [File]

    # Keep only duplicate entries
    Result = {}

    for Key in DuplicateFiles:

        if len(DuplicateFiles[Key]) > 1:
            Result[Key] = DuplicateFiles[Key]

    return Result


#----------------------------------------------------------
# Testing
#----------------------------------------------------------
"""
if __name__ == "__main__":

    Directory = input("Enter directory path : ")

    Result = FindDuplicate(Directory)

    if len(Result) == 0:
        print("\nNo duplicate files found.")
    else:
        print("\nDuplicate Files Found\n")

        Count = 1

        for Checksum, Files in Result.items():

            print("--------------------------------------")
            print("Duplicate Group :", Count)
            print("Checksum :", Checksum)

            for File in Files:
                print(File)

            Count = Count + 1

"""