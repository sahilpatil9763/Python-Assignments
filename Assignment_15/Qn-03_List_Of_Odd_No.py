# Write a lambda function using filter() which accepts a list of numbers and returns list of odd numbers.

Odd = lambda No : No % 2 != 0

def main():
    
    Data = list(int(x) for x in input("Enter numbers separated by space: ").split())
    
    FData = list(filter(Odd, Data))
    
    print("Odd numbers are:", FData)
    

if __name__ == "__main__":
    main()