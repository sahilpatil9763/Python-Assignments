"""
Q5) Frequency of a String in File 
Problem Statement: Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file. 
Input: Demo.txt Marvellous Expected 
Output: Count how many times "Marvellous" appears in Demo. txt.
"""

def Frequency(FileName, Word):
    try:
        file = open(FileName, "r")

        count = 0

        for line in file:
            words = line.split()

            for w in words:
                if w == Word:
                    count += 1

        file.close()

        print("Frequency of", Word, "is:", count)

    except FileNotFoundError:
        print("File not found.")


def main():
    Name = input("Enter file name: ")
    Search = input("Enter string: ")

    Frequency(Name, Search)


if __name__ == "__main__":
    main()