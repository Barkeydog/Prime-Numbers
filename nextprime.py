from sympy import nextprime

num_digits = 1500
large_prime = nextprime(10**(num_digits-1))

print(f"The prime number with over {num_digits} digits is:")
print(large_prime)
