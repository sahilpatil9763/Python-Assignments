"""
Design a Python application that creates two separate threads named Even and Odd.
• The Even thread should display the first 10 even numbers.
• The Odd thread should display the first 10 odd numbers.
• Both threads should execute independently using the threading module.
• Ensure proper thread creation and execution.
"""

import threading

def Even(No):
    for i in range(1, No+1):
        Num = i * 2
        print("Even Number : ",Num)

def Odd(No):
    for i in range(1, No+1):
        Num = (i * 2) - 1
        print("Odd Number : ",Num)

def main():
    
    print("\n-------- Start of Thread 1 --------\n")

    t1 = threading.Thread(target=Even, args=(10,))
    t1.start()
    t1.join()

    print("\n--------- End of Thread 1 ---------\n")

    print("\n-------- Start of Thread 2 ---------\n")

    t2 = threading.Thread(target=Odd, args=(10,))
    t2.start()
    t2.join()

    print("\n--------- End of Thread 2 ---------\n")

if __name__ == "__main__":
    main()