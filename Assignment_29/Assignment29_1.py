"""
Q1) Check File Exists in Current Directory
Problem Statement: Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.
Input: Demo.txt
Expected Output: Display whether Demo. txt exists or not.
"""

import os

def CheckFile(FileName):
    if os.path.exists(FileName):
        print(f"{FileName} exists")
    else:
        print(f"{FileName} does not exists")

def main():
    Name = input("Enter File Name : ")
    CheckFile(Name)

if __name__ == "__main__":
    main()