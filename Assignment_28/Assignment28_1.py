"""
Q1) Count Lines in a File
Problem Statement: Write a program which accepts a file name from the user and counts how many lines are present in the file.
Input: Demo.txt
Expected Output: Total number of lines in Demo. txt.
"""

import os

def CreateFile(FileName):
    try:
        fObj = open(FileName,"w")
        fObj.write("Marvellous Infosystems")

        fObj = open(FileName,"r")
        lines = fObj.readlines()

        print("Total number of lines in ",FileName, " : ", len(lines))
        
        fObj.close()

    except FileNotFoundError as fObj:
        print("File is not present in current directory")

def main():
    Name = input("Enter file name : ")
    CreateFile(Name)

if __name__ == "__main__":
    main()