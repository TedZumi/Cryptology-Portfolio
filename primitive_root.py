from Euler import euler_function
from prime import prime_factors
from Euclid_algoritm import extended_gcd


def calculate_primitive_root(m):
    if len(prime_factors(m)) != 1:
        return None

    b = True
    a = 2
    while b:
        nod = extended_gcd(a, m)[0]
        if nod != 1:
            continue
        else:
            euler_f = euler_function(m)
            factors = prime_factors(euler_f)
            degrees = find_combinations(factors)
            count = 0
            for degree in degrees:
                temp = a ** degree % m
                if temp == 1:
                    count += 1
            if count == 1:
                b = False
            else:
                a += 1
    return a


def find_combinations(numbers):
    combinations_list = []
    for i in range(len(numbers) + 1):
        for j in range(i):
            combination = [numbers[k] for k in range(j, i)]
            product = 1
            for num in combination:
                product *= num
            if product not in combinations_list:
                combinations_list.append(product)
    combinations_list.sort()
    return combinations_list


def reduced_deduction_system(m):
    a = calculate_primitive_root(m)
    print(f"Первообразный корень: {a}")
    if a:
        euler_f = euler_function(m)
        U = []
        for i in range(euler_f - 1):
            U.append(a ** i % m)
        return U
    else:
        return None


# m = int(input("Введите модуль: "))
# a = calculate_primitive_root(m)
# print(f"Первообразный корень: {a}")
# # while m != 0:
# #     a = calculate_primitive_root(m)
# #     if a:
# #         print(f"Первообразный корень: {a}")
# #     else:
# #         print(f"первообразный корень не существует")
# #     m = int(input("Введите модуль: "))
# while m != 0:
#     U = reduced_deduction_system(m)
#     if U:
#         print(f"Приведенная система вычетов по m: {U}")
#     else:
#         print(f"Первообразного корня по m не существует")
#     m = int(input("Введите модуль: "))