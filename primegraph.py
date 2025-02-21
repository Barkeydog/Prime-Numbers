import matplotlib.pyplot as plt
from sympy import primerange

def generate_primes(limit):
    primes = list(primerange(1, limit))
    return primes

limit = 100
primes = generate_primes(limit)

positions = list(range(1, len(primes) + 1))

plt.plot(positions, primes, marker='o', linestyle='-', color='b')
plt.title('Prime Numbers Plot')
plt.xlabel('Position in List of Primes')
plt.ylabel('Prime Number')
plt.grid(True)
plt.show()
