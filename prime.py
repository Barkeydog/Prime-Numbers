import sympy

def find_prime(n):
    lower_bound = 10**(n - 1)
    upper_bound = 10**n - 1

    while True:
        candidate = sympy.randprime(lower_bound, upper_bound)
        if candidate % 2 == 0:
            continue

        if sympy.isprime(candidate):
            return candidate

if __name__ == "__main__":
    num_digits = 2500
    prime_number = find_prime(num_digits)
    print(f"The prime number with {num_digits} digits (excluding even numbers) is:\n{prime_number}")
