def gen_primes():
  D = {}
  q = 2
  while True:
      if q not in D:
          D[q * q] = [q]
          yield q
      else:
          for p in D[q]:
              D.setdefault(p + q, []).append(p)
          del D[q]
      q += 1
