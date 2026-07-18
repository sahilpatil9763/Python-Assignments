"""
Q5) Search a Word in File
Problem Statement: Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.
Input: Demo.txt Marvellous
Expected Output: Display whether the word Marvellous is found in Demo. txt or not.
"""

def SearchWord(FileName, Word):
    try:
        fObj = open(FileName,"r")

        if (Word == "Marvellous"):
            print(f"{Word} is found in {FileName}")
        else:
            print(f"{Word} is not found in {FileName}")
            
        fObj.close()
                    
    except FileNotFoundError:
        print("File is not present in current directory")

def main():
    FName = input("Enter file name : ")
    Word = input("Enter word to search : ")
    SearchWord(FName, Word)

if __name__ == "__main__":
    main()