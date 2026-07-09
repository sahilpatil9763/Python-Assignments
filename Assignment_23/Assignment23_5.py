"""
Write a program that calculates factorials of multiple numbers
simultaneously using multiprocessing.Pool.

Input
Data = 110, 15, 20, 25]

Expected Task
For every N, calculate:
N!

Expected Output Format
Process ID : 1240
Input Number : 20
Factorial : 2432902008176640000
"""

import multiprocessing
import time
import os

def Factorial(No):
    #print("Process is running with PID : ", os.getpid())

    Ans = 1

    for i in range(1, No + 1):
        Ans = Ans * i
    
    print("\nProcess ID : ", os.getpid())
    print("Input Number : ",No)
    print("Factorial : ",Ans)

    return Ans
    
def main():
    n = int(input("Enter number of elements: "))

    Data = []

    start_time = time.perf_counter()

    print("Enter elements:")
    for i in range(n):
        Data.append(int(input()))

    print("\nInput numbers are : ",Data)

    pObj = multiprocessing.Pool()

    Result = pObj.map(Factorial, Data)

    pObj.close()
    pObj.join()

    end_time = time.perf_counter()

    print("\nResult List : ",Result)
    print(f"\nTime required : {end_time - start_time:.4f} seconds\n")

if __name__ == "__main__":
    main()