"""
Module Name : Checksum.py

Description :
This module contains functions to calculate the checksum
(MD5) of a file. The checksum is used to identify duplicate files.
"""

import hashlib
import os


#----------------------------------------------------------
# Function Name : CalculateChecksum
# Description   : Returns MD5 checksum of a file
# Input         : Absolute file path
# Output        : MD5 checksum (string)
#----------------------------------------------------------

def CalculateChecksum(FileName):

    if os.path.isfile(FileName) == False:
        return None

    hashobj = hashlib.md5()

    try:
        fd = open(FileName, "rb")

        Buffer = fd.read(1024)

        while len(Buffer) > 0:
            hashobj.update(Buffer)
            Buffer = fd.read(1024)

        fd.close()

        return hashobj.hexdigest()

    except Exception as e:
        print("Unable to calculate checksum :", e)
        return None


#----------------------------------------------------------
# For Testing Purpose
#----------------------------------------------------------
"""
if __name__ == "__main__":

    FilePath = input("Enter file name : ")

    Result = CalculateChecksum(FilePath)

    if Result != None:
        print("MD5 :", Result)

"""