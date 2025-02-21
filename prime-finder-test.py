def is_prime(num):
  if num < 2:
      return False
  for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
          return False
  return True

x = 1

while True:
  y = (2 ** x - 1) / 24
  if y.is_integer():
      y = int(y)
      value_24y_plus_1 = 24 * y + 1
      print(f"Value of 24y + 1 for x={x}: {value_24y_plus_1}")

      if is_prime(value_24y_plus_1):
          print(f"24y + 1 is prime for x={x}")
      else:
          print(f"24y + 1 is not prime for x={x}")

  x += 1
