"""
Write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for every element in the list.

Example Input
[1000000,2000000,3000000,4000000]

Expected Output
[333333833333500000,
2666668666667000000,
・・・
]
"""

import multiprocessing
import time
import os

def SumSquare(No):
    print("Process is running with PID : ", os.getpid())
    Sum = 0

    for i in range(1, No+1):
        Sum = Sum + (No ** 2)
    return Sum

def main():
    n = int(input("Enter number of elements: "))

    Data = []

    start_time = time.perf_counter()

    print("Enter elements:")
    for i in range(n):
        Data.append(int(input()))

    pObj = multiprocessing.Pool()

    Result = pObj.map(SumSquare, Data)

    pObj.close()
    pObj.join()

    end_time = time.perf_counter()

    print(Result)
    print(f"Time required : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()