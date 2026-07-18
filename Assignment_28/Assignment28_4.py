"""
Q4) Copy File Contents into Another File
Problem Statement: Write a program which accepts two file names from the us
    • First file is an existing file
    • Second file is a new file
Copy all contents from the first file into the second file.
Input : ABC. txt Demo.txt
Expected Output : Contents of ABC.txt copied into Demo.txt
"""

def CopyFile(SourceFile, DestinatinoFile):
    try:
        sObj = open(SourceFile,"r")
        dObj = open(DestinatinoFile,"w")

        for lines in sObj:
            dObj.write(lines)
        
        sObj.close()
        dObj.close()

        print(f"Contents of {SourceFile} copied into {DestinatinoFile}")
                    
    except FileNotFoundError:
        print("File is not present in current directory")

def main():
    Source = input("Enter existing file name : ")
    Destination = input("Enter new file name : ")
    CopyFile(Source, Destination)

if __name__ == "__main__":
    main()