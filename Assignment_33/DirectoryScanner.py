"""
Module Name : DirectoryScanner.py

Description :
This module scans a directory recursively and
returns the list of all files.
"""

import os


#----------------------------------------------------------
# Function Name : ScanDirectory
# Description   : Recursively scans a directory
# Input         : Directory Path
# Output        : List of files
#----------------------------------------------------------

def ScanDirectory(DirectoryName):

    FileList = []

    # Check whether directory exists
    if os.path.exists(DirectoryName) == False:
        print("Error : Directory does not exist.")
        return FileList

    # Check whether it is really a directory
    if os.path.isdir(DirectoryName) == False:
        print("Error : Invalid directory.")
        return FileList

    # Convert into absolute path
    DirectoryName = os.path.abspath(DirectoryName)

    # Recursive scanning
    for FolderName, SubFolders, Files in os.walk(DirectoryName):

        for File in Files:

            AbsolutePath = os.path.join(FolderName, File)

            FileList.append(AbsolutePath)

    return FileList


#----------------------------------------------------------
# Testing
#----------------------------------------------------------
"""
if __name__ == "__main__":

    Directory = input("Enter directory path : ")

    Result = ScanDirectory(Directory)

    print("\nTotal Files :", len(Result))

    print("\nList Of Files\n")

    for File in Result:
        print(File)

"""