"""
Q2) Count Words in a File
Problem Statement: Write a program which accepts a file name from the user and counts the total number of words in that file.
Input: Demo.txt
Expected Output: Total number of words in Demo. txt.
"""

import os

def CountWords(FileName):
    try:
        fObj = open(FileName,"r")

        count = 0
        for lines in fObj:
            words = lines.split()
            count = count + len(words)
        
        fObj.close()
            
        print("Total number of words in ",FileName, " : ", count)
        
    except FileNotFoundError as fObj:
        print("File is not present in current directory")

def main():
    Name = input("Enter file name : ")
    CountWords(Name)

if __name__ == "__main__":
    main()