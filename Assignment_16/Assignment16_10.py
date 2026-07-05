"""
Program which accept name from user and siplay length of that name.
"""

def LenghtName(Name):
    return len(Name)

def main():
    Name = input("Enter a name: ")
    print(LenghtName(Name))

if __name__ == "__main__":
    main()
