"""
Q2) Display File Contents
Problem Statement: Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.
Input: Demo.txt
Expected Output: Display contents of Demo. txt on console.
"""

import os

def DisplayFile(FileName):
    if os.path.exists(FileName):
        fObj = open(FileName, "r")

        Data = fObj.read()

        print(Data)

    else:
        print("File does not exist.")

def main():
    Name = input("Enter File Name : ")
    DisplayFile(Name)

if __name__ == "__main__":
    main()