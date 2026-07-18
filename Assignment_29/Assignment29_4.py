"""
Q4) Compare Two Files (Command Line)
Problem Statement: Write a program which accepts two file names through command line arguments and compares the contents of both files.
• If both files contain the same contents, display Success
• Otherwise display Failure
Input (Command Line):
Demo.txt Hello.txt
Expected Output:Success OR Failure
"""

import sys

def CompareFile(File1, File2):
    try:
        fObj1 = open(File1, "r")
        fObj2 = open(File2, "r")

        Data1 = fObj1.read()
        Data2 = fObj2.read()

        if (Data1 == Data2):
            print("Successs")
        else:
            print("Failure")

        fObj1.close()
        fObj2.close()

    except FileNotFoundError:
        print("File not found.")


def main():
    CompareFile(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()