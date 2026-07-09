"""
Write a Python program using multiprocessing. Pool to calculate the sum of all even numbers from 1 to n for every number from the given list.

Input
Data = [1000000, 2000000, 3000000, 4000000]

Expected Task
For each number N, calculate:
2+ 4 + 6 + • • + N

Expected Output Format
Process ID : 1234
Input Number : 1000000
Sum of Even Numbers : 250000500000
"""

import multiprocessing
import time
import os

def SumEven(No):
    print("Process is running with PID : ", os.getpid())

    Sum = 0

    for i in range(2, No + 1, 2):
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

    Result = pObj.map(SumEven, Data)

    pObj.close()
    pObj.join()

    end_time = time.perf_counter()

    print("\nResult List : ",Result)
    print(f"\nTime required : {end_time - start_time:.4f} seconds\n")

if __name__ == "__main__":
    main()