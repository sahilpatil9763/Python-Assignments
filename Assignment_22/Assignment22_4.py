"""
Write a program that calculates
1^5+2^5+3^5+.....+N^5
for multiple values of N simultaneously using Pool.

Input
[1000000,2000000,3000000,4000000]

Measure total execution time.
"""

import multiprocessing
import time
import os

def SumRaiseToFive(No):
    print("Process is running with PID : ", os.getpid())

    Sum = 0

    for i in range(1, No+1):
        Sum = Sum + (i ** 5)
    return Sum
    
def main():
    n = int(input("Enter number of elements: "))

    Data = []

    start_time = time.perf_counter()

    print("Enter elements:")
    for i in range(n):
        Data.append(int(input()))

    print("Input numbers are : ",Data)

    pObj = multiprocessing.Pool()

    Result = pObj.map(SumRaiseToFive, Data)

    pObj.close()
    pObj.join()

    end_time = time.perf_counter()

    print("Total prime count of each number : ",Result)
    print(f"Time required : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()