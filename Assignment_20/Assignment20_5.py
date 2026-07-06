"""
Design a Python application that creates two threads named Thread1 and Thread2.
• Thread1 should display numbers from 1 to 50.
• Thread2 should display numbers from 50 to 1 in reverse order.
• Ensure that:
    • Thread2 starts execution only after Threadl has completed.
• Use appropriate thread synchronization
"""

import threading

def Thread1(No):
    print("\nThread1 Started")
    for i in range(1, No+1):
        print(i, end=" ")
        
    print()

def Thread2(No):
    print("\nThread2 Started")
    for i in range(No, 0, -1):
        print(i,end=" ")
    print()
    
def main():

    Value = int(input("Enter a number: "))

    t1 = threading.Thread(target=Thread1, args=(Value,))
    t2 = threading.Thread(target=Thread2, args=(Value,))
    
    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()