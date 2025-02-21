import matplotlib.pyplot as plt

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def list_primes(start, end):
    primes = []
    total_numbers = 0
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
        total_numbers += 1
    return primes, total_numbers

def plot_primes(prime_list, total_numbers):
    x = list(range(1, len(prime_list) + 1))
    plt.scatter(x, prime_list, color='red', marker='o')
    plt.title('Prime Numbers')
    plt.xlabel('Index')
    plt.ylabel('Prime Number')
    plt.grid(True)
    plt.xlim(0, len(prime_list) + 1)
    plt.ylim(0, max(prime_list) + 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

start_range = 1
end_range = 1000000
primes, total_numbers = list_primes(start_range, end_range)
ratio_percentage = len(primes) / total_numbers * 100
print(f"The ratio of prime numbers to total numbers is: {ratio_percentage:.2f}%")
plot_primes(primes, total_numbers)


