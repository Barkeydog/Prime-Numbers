import math
import random

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime(digit_length):
    """Generate a prime number with a specific digit length."""
    if digit_length < 1:
        print("Digit length must be at least 1.")
        return None

    start = 10**(digit_length - 1)
    end = 10**digit_length - 1

    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

def main():
    try:
        digit_length = int(input("Enter the number of digits: "))
        prime = generate_prime(digit_length)
        if prime:
            print(f"A prime number with {digit_length} digits: {prime}")
        else:
            print(f"No prime number found with {digit_length} digits.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
