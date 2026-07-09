"""
Write a Python program using multiprocessing. Pool to calculate the sum of all odd numbers from 1 to n.

Input
Data = [1000000, 2000000, 3000000, 4000000]

Expected Task

For each number N, calculate:
1 + 3 + 5+ … ..+ N

Expected Output Format

Process ID : 1235
Input Number : 1000000
Sum of Odd Numbers : 250000000000
"""

import multiprocessing
import time
import os

def SumOdd(No):
    print("Process is running with PID : ", os.getpid())

    Sum = 0

    for i in range(1, No + 1, 2):
        Sum = Sum + i
    
    print("\nProcess ID : ", os.getpid())
    print("Input Number : ",No)
    print("Sum of Even Numbers : ",Sum)

    return Sum
    
def main():
    n = int(input("Enter number of elements: "))

    Data = []

    start_time = time.perf_counter()

    print("Enter elements:")
    for i in range(n):
        Data.append(int(input()))

    print("\nInput numbers are : \n",Data)

    pObj = multiprocessing.Pool()

    Result = pObj.map(SumOdd, Data)

    pObj.close()
    pObj.join()

    end_time = time.perf_counter()

    print("\nResult List : ",Result)
    print(f"\nTime required : {end_time - start_time:.4f} seconds\n")

if __name__ == "__main__":
    main()