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


N = 509
factors = prime_factors(N)
factor_counts = create_factor_counts(factors)
print(f"{N} = ", end='')
for factor in prime_factors(N):
    print(f"{factor}", end=' ')
print(f"\nСтепени множителей: {factor_counts}")