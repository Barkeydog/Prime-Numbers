def is_prime(n):
  if n <= 1:
      return False
  for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
          return False
  return True

def lucas_lehmer(p):
  if p == 2:
      return True

  s = 4
  M = 2**p - 1

  for _ in range(2, p):
      s = (s**2 - 2) % M

  return s == 0

def test_mersenne_prime(p):
  if is_prime(p):
      mersenne_number = 2**p - 1
      if lucas_lehmer(p):
          return mersenne_number, len(str(mersenne_number))
  return None

def find_mersenne_primes(limit):
  p = 2
  while True:
      mersenne_prime_info = test_mersenne_prime(p)
      if mersenne_prime_info:
          mersenne_prime, prime_length = mersenne_prime_info
          print(f"{mersenne_prime} (Length: {prime_length} digits)")
      p += 1
      if p > limit:
          break

limit_value = int(input("Enter the limit for testing Mersenne primes: "))
find_mersenne_primes(limit_value)
