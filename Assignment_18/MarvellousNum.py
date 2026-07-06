# File Name: MarvellousNum.py

def ChkPrime(num):
    # Numbers less than or equal to 1 are never prime
    if num <= 1:
        return False
    
    # Check if 'num' can be divided evenly by any number from 2 up to num-1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # Found a divisor! It is NOT prime.
            
    return True  # No divisors found! It IS prime.