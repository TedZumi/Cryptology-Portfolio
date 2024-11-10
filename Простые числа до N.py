import random
from LegendreJacobian import calculateJacobian, prime_factors, extended_gcd


# mod = modulo(a, (p - 1) / 2, p)
# Generate a random number a
        # a = random.randrange(p - 1) + 1

# modulo function to perform binary
# exponentiation
def modulo(base, exponent, mod):
    x = 1
    y = base
    while (exponent > 0):
        if (exponent % 2 == 1):
            x = (x * y) % mod
        y = (y * y) % mod
        exponent = exponent // 2
    return x % mod


# To perform the Solovay- Strassen
# Primality Test
def solovoyStrassen(p, iterations):
    if (p < 2):
        return False
    if (p != 2 and p % 2 == 0):
        return False

    for i in range(iterations):
        a = random.randrange(p - 1) + 1
        # print(f"a = {a}")
        factors = prime_factors(a)
        if len(factors) > 1:
            nod, x_1, y_1 = extended_gcd(a, p)
            # print(nod)
            if nod != 1:
                # print(f"{a} и {p} не взаимно простые, символ Якоби посчитать нельзя")
                return False
            else:
                jacobian = calculateJacobian(a, factors)
                # print(f"jacobian = {jacobian}")
                mod = a**((p-1) // 2) % p
                while mod != -1 and mod != 1:
                    mod -= p
                # print(f"mod = {mod}")
                if (jacobian == 0 or mod != jacobian):
                    return False
    return True


# Driver Code
# iterations = 15
# num1 = 7

# if (solovoyStrassen(num1, iterations)):
#     print(num1, "is prime ")
# else:
#     print(num1, "is composite")

n = int(input("Введите n: "))
primes = []
for i in range(1, n+1):
    iterations = 5
    if solovoyStrassen(i, iterations):
        primes.append(i)
print(f"Простые числа: {primes}")
