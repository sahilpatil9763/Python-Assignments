"""
Design a Python application that creates three threads named Small, Capital, and Digits.
• All threads should accept a string as input.
• The Small thread should count and display the number of lowercase characters.
• The Capital thread should count and display the number of uppercase characters.
• The Digits thread should count and display the number of numeric digits.
• Each thread must also display:
    • Thread ID
    • Thread Name
"""

import threading
import time

def Small(Text):
    count = 0
    for char in Text:
        if char.islower():
            count = count + 1 

    print("\nTID of Small Thread : ",threading.get_ident())
    print("Thread name is : ",threading.current_thread().name)
    print("Count of lower case character : ",count)    

def Capital(Text):
    count = 0
    for char in Text:
        if char.isupper():
            count = count + 1 
    
    print("\nTID of Capital Thread : ",threading.get_ident())
    print("Thread name is : ",threading.current_thread().name)
    print("Count of upper case character : ",count)

def NumericDigits(Text):
    count = 0
    for char in Text:
        if char.isdigit():
            count = count + 1 
    
    print("\nTID of NumericDigits Thread : ",threading.get_ident())
    print("Thread name is : ",threading.current_thread().name)
    print("Count of Neric Digits : ",count)


def main():

    String = input("Enter a string: ")

    start_time = time.perf_counter()

    t1 = threading.Thread(target=Small, args=(String,))
    t1.start()
    t1.join()

    t2 = threading.Thread(target=Capital, args=(String,))
    t2.start()
    t2.join()

    t3 = threading.Thread(target=NumericDigits, args=(String,))
    t3.start()
    t3.join()

    end_time = time.perf_counter()

    print(f"Time is {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()