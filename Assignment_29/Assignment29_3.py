"""
Q3) Copy File Contents into a New File (Command Line)
Problem Statement: Write a program which accepts an existing file name through command line arguments, creates a new file named Demo. txt, and copies all contents from the given file into Demo. txt.
Input (Command Line): ABC.txt
Expected Output: Create Demo. txt and copy contents of ABC. txt into Demo. txt.
"""

import sys

def CopyFile(SourceFile):
    try:
        source = open(SourceFile, "r")
        destination = open("Demo.txt", "w")

        for line in source:
            destination.write(line)

        source.close()
        destination.close()

        print("Contents copied successfully into Demo.txt.")

    except FileNotFoundError:
        print("Source file not found.")


def main():
    CopyFile(sys.argv[1])


if __name__ == "__main__":
    main()