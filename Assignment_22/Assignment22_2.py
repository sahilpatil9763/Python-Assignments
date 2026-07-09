"""
Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().

Input
[10,15,20,25]

Display
• Process ID
• Input Number
• Factorial
"""

import multiprocessing
import time
import os

def Factorial(No):
    print("Process is running with PID : ", os.getpid())

    Ans = 1
    for i in range(1, No + 1):
        Ans = Ans * i
    return Ans  

def main():
    n = int(input("Enter number of elements: "))

    Data = []

    start_time = time.perf_counter()

    print("Enter elements:")
    for i in range(n):
        Data.append(int(input()))

    print("Input numbers are : ",Data)

    pObj = multiprocessing.Pool()

    Result = pObj.map(Factorial, Data)

    pObj.close()
    pObj.join()

    end_time = time.perf_counter()

    print("Factorial : ",Result)
    print(f"Time required : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()