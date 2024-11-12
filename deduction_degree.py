from system_comparison import calculate_comparison_system
from prime import prime_factors
from Euclid_algoritm import extended_gcd


def deduction_degree(a, k, m):
    factors = prime_factors(m)
    print(f"{m} = {factors}")
    if len(factors) == 1:
        degrees = k % (m - 1)
        print(f"{k} mod ({m}-1) = {degrees}")
        return a ** degrees % m
    else:
        system = {}
        i = 1
        for item in factors:
            degrees = k % (item - 1)
            print(f"{a} mod ({m}-1) = {degrees}")
            system[i] = [1, a**degrees, item]
            i += 1

        print("Система сравнений:")
        for key in system:
            print(f"{system[key][0]}x={system[key][1]}(mod {system[key][2]})")

        print("\nРешение системы сравнений:")
        x = calculate_comparison_system(system)
        return x


a, k, m = map(int, input(f"Вычет: a^k(mod m) Введите a, k, m: ").split())
nod = extended_gcd(a, m)[0]
if nod != 1:
    print(f"a и m не взаимно простые")
else:
    result = deduction_degree(a, k, m)
    print(f"\nВычет: {a}^{k}(mod {m}) = {result}")

