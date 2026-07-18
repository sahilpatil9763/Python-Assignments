"""
Q3) Display File Line by Line
Problem Statement: Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.
Input: Demo.txt
Expected Output: Display each line of Demo. txt one by one.
"""

def Display(FileName):
    try:
        fObj = open(FileName,"r")

        for lines in fObj:
            print(lines, end="")
        
        fObj.close()
                    
    except FileNotFoundError as fObj:
        print("File is not present in current directory")

def main():
    Name = input("Enter file name : ")
    Display(Name)

if __name__ == "__main__":
    main()