"""
Module Name : FileRemover.py

Description :
This module removes duplicate files while
keeping one original copy.
"""

import os


#----------------------------------------------------------
# Function Name : RemoveDuplicateFiles
# Description   : Deletes duplicate files
# Input         : Duplicate Dictionary
# Output        : List of deleted files
#----------------------------------------------------------

def RemoveDuplicateFiles(DuplicateDictionary):

    DeletedFiles = []

    # Traverse every duplicate group
    for Checksum, FileList in DuplicateDictionary.items():

        # Keep first file, delete remaining
        for File in FileList[1:]:

            try:
                os.remove(File)

                DeletedFiles.append(File)

                print("Deleted :", File)

            except Exception as e:
                print("Unable to delete :", File)
                print("Reason :", e)

    return DeletedFiles


#----------------------------------------------------------
# Testing
#----------------------------------------------------------
"""
if __name__ == "__main__":

    from DuplicateFinder import FindDuplicate

    Directory = input("Enter directory path : ")

    DuplicateData = FindDuplicate(Directory)

    if len(DuplicateData) == 0:
        print("\nNo duplicate files found.")

    else:

        Deleted = RemoveDuplicateFiles(DuplicateData)

        print("\n--------------------------------")
        print("Total Deleted :", len(Deleted))

"""