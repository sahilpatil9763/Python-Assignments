# Write a lambda function using map() which accepts a list of numbers and returns their squares of each number.

Square = lambda No : No ** 2

def main():
    
    Data = list(int(x) for x in input("Enter numbers separated by space: ").split())
        
    MData = list(map(Square, Data))
    
    print("Square of each number is:", MData)
    

if __name__ == "__main__":
    main()