def is_prime(num):
  if num < 2:
      return False
  for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
          return False
  return True

def main():
  n = int(input("Enter the value of n: "))

  result = 2 ** n - 1

  if is_prime(result):
      print(f"{result} is a prime number.")
      print(f"Length of the prime number in digits: {len(str(result))}")
  else:
      print(f"{result} is not a prime number.")

if __name__ == "__main__":
  main()
