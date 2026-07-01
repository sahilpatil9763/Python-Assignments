"""
Write a lambda function using filter() which accepts a list of strings and returns strings with length greater than 5.
"""
    
String_Length = lambda s : len(s) > 5

def main():
    
    Data = list(input("Enter strings separated by space: ").split())
    
    FData = list(filter(String_Length, Data))
    
    print("Strings with length greater than 5 are: ", FData)
    

if __name__ == "__main__":
    main()