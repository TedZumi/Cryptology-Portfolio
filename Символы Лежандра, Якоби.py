def calculateLegendre(q, p):
    temp = 1
    if q == 0:
        return 0  # (0/p) = 0

    if q < 0:
        # (q/p) = (-q/p)*(-1/p)
        q = -q
        temp *= (-1) ** ((p - 1) // 2)
        temp *= calculateLegendre(q, p)

    print(f"q = {q}, p = {p}, temp = {temp}")
    q %= p
    print(f"q = {q}, p = {p}, temp = {temp}")

    factors = prime_factors(q)
    factor_counts = create_factor_counts(factors)
    print(factor_counts)
    for key, value in factor_counts.items():
        print("key:", key, "value:", value)
        if (key == 2) and (value % 2 != 0):
            rezult = 2 ** ((p - 1) // 2) % p
            while rezult != -1 and rezult != 1:
                rezult -= p
            temp *= rezult
            print("temp:", temp)
        elif value % 2 != 0:
            temp *= (-1) ** (((key - 1) // 2) * ((p - 1) // 2))
            print("temp:", temp)
            temp *= calculateLegendre(p, key)
            print("temp:", temp)

    return temp


def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    return factors


def create_factor_counts(factors):
    factor_counts = {}
    for factor in factors:
        if factor in factor_counts:
            factor_counts[factor] += 1
        else:
            factor_counts[factor] = 1
    return factor_counts


def calculateJacobian(q, factors):
    temp = 1
    for factor in factors:
        temp *= calculateLegendre(q, factor)
    return temp


def extended_gcd(a, b):
    x_1, x_2 = 1, 0
    y_1, y_2 = 0, 1
    i = 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        x_1, x_2 = x_2, x_1 - q * x_2
        y_1, y_2 = y_2, y_1 - q * y_2
        i += 1
    return a, x_1, y_1


a, b = map(int, input("Введите число и модуль: ").split())
factors = prime_factors(b)
if len(factors) > 1:
    nod, x_1, y_1 = extended_gcd(a, b)
    if nod != 1:
        print(f"{a} и {b} не взаимно простые, символ Якоби посчитать нельзя")
    else:
        print(f"Символ Якоби {a}/{b} = {calculateJacobian(a, factors)}")
else:
    print(f"Символ Лежандра {a}/{b} = {calculateLegendre(a, b)}")