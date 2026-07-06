"""
Accept N number from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. Name of the function from main pyhton file should be ListPrime()
Input: Number of elements: 11
Input Elements: 13 5 45 7 4 56 10 34 2 5 8
Output: 54(13 + 5 + 7 + 2 + 5)
"""

# File Name: Assignment18_5.py
import MarvellousNum

def ListPrime(elements):
    prime_numbers = []
    
    # Collect all prime numbers from the list
    for num in elements:
        if MarvellousNum.ChkPrime(num):
            prime_numbers.append(num)
            
    # Calculate the true sum
    total_sum = sum(prime_numbers)
    
    # Return the sum
    return total_sum

def main():
    n = int(input("Number of elements : "))
    elements = list(map(int, input("Input Elements : ").split()))
    
    total = ListPrime(elements)
    
    # Print the output matching the assignment's format (with the correct sum!)
    print(f"Output : {total}")

if __name__ == "__main__":
    main()