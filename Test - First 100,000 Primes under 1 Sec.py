import time
from math import isqrt

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def find_primes(limit):
    """Find the first `limit` prime numbers."""
    primes = []
    num = 2  # Start checking from the first prime number
    while len(primes) < limit:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

if __name__ == "__main__":
    start_time = time.time()
    first_10000_primes = find_primes(10000)
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"Time to compute 10,000 primes: {elapsed_time:.2f} seconds")
    # Optional: Uncomment to print the primes
    # print(first_10000_primes)
