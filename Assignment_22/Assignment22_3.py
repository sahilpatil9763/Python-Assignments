"""
For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing Pool.

Example
10000
20000
30000
40000

Display total prime count for each number.
"""

import multiprocessing
import time
import os

def Prime(No):
    #print("Process is running with PID : ", os.getpid())

    if No <= 1:
        return False
    
    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False
        
        return True
    
def CountPrime(Num):
    Count = 0

    for i in range(1, Num + 1):
        if Prime(i):
            Count = Count + 1

    return Count

def main():
    n = int(input("Enter number of elements: "))

    Data = []

    start_time = time.perf_counter()

    print("Enter elements:")
    for i in range(n):
        Data.append(int(input()))

    print("Input numbers are : ",Data)

    pObj = multiprocessing.Pool()

    Result = pObj.map(CountPrime, Data)

    pObj.close()
    pObj.join()

    end_time = time.perf_counter()

    print("Total prime count of each number : ",Result)
    print(f"Time required : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()