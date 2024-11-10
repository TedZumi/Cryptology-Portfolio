from prime_factors import *


def euler_function(p):
    factors = prime_factors(p)
    print(f"Простые множители: {factors}")
    euler = 1
    if len(factors) == 1:
        return p - 1
    else:
        factor_counts = create_factor_counts(factors)
        print(f"Степени простых множителей: {factor_counts}")
        for key, value in factor_counts.items():
            print(f"p = {key}, k = {value}")
            f_1 = key ** value
            f_2 = key ** (value - 1)
            print(f"{f_1}, {f_2}, ", end = " ")
            euler = euler * (f_1 - f_2)
            print(f"f = {euler}")
        return euler


def is_prime(n):
  if n <= 1:
    return False

  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False

  return True


print(f"Функция Эйлера: {euler_function(400)}")