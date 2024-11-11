from prime import prime_factors
from reverse_element import reverse_element
from Euclid_algoritm import extended_gcd


def calculate_comparison(a, b, m):
    factors = prime_factors(m)
    if len(factors) == 1:
        a %= m
        b %= m
        u = reverse_element(a, m)
        a *= u
        b *= u
        a %= m
        b %= m
        return b, 1
    else:
        nod = extended_gcd(a, m)[0]
        if b % nod == 0:
            a /= nod
            b /= nod
            m /= nod

            a %= m
            b %= m
            u = reverse_element(a, m)
            a *= u
            b *= u
            a %= m
            b %= m
            return b, nod
        else:
            return 0, 0


a, b, m = map(int, input("Сравнение: ax=b(mod m) Введите a, b, m: ").split())
result, count = calculate_comparison(a, b, m)
if count == 0:
    print(f"Сравнение {a}x={b}(mod {m}) не имеет решений")
else:
    m /= count
    m = int(m)
    for i in range(count):
        print(f"{i + 1} решение: x = {result} + {m}*k, k - целое")
        result += m