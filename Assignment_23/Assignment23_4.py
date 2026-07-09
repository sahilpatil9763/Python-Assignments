"""
Write a program that counts how many odd numbers exist between
1 and N.

Input
Data = [1000000, 2000000, 3000000, 4000000]

Expected Output Format
Process ID : 1237
Input Number : 1000000
Odd Number Count : 500000
"""

import multiprocessing
import time
import os

def CountOdd(No):
    #print("Process is running with PID : ", os.getpid())

    Count = 0

    for i in range(1, No + 1, 2):
        Count = Count + 1
    
    print("\nProcess ID : ", os.getpid())
    print("Input Number : ",No)
    print("Count of Odd Numbers : ",Count)

    return Count
    
def main():
    n = int(input("Enter number of elements: "))

    Data = []

    start_time = time.perf_counter()

    print("Enter elements:")
    for i in range(n):
        Data.append(int(input()))

    print("\nInput numbers are : ",Data)

    pObj = multiprocessing.Pool()

    Result = pObj.map(CountOdd, Data)

    pObj.close()
    pObj.join()

    end_time = time.perf_counter()

    print("\nResult List : ",Result)
    print(f"\nTime required : {end_time - start_time:.4f} seconds\n")

if __name__ == "__main__":
    main()