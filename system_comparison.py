from comparison import calculate_comparison
from reverse_element import reverse_element
from Euclid_algoritm import extended_gcd


def are_coprime(numbers):
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            nod = extended_gcd(numbers[i], numbers[j])[0]
            if nod != 1:
                return False
    return True


def calculate_comparison_system(system):
    M = 1
    for key in system:
        M *= system[key][2]

    table = {}
    for key in system:
        b_key = calculate_comparison(system[key][0], system[key][1], system[key][2])[0]
        m_key = system[key][2]
        M_key = int(M / m_key)
        y_key = reverse_element((M_key % m_key), m_key)
        print(f"b[{key}] = {b_key}, m[{key}] = {m_key}, M[{key}] = {M_key}, y[{key}] = {y_key}")
        table[key] = [b_key, m_key, M_key, y_key]

    x = 0
    for key in table:
        temp = table[key][0] * table[key][2] * table[key][3]
        print(f"{table[key][0]} * {table[key][2]} * {table[key][3]} = {temp}")
        x += temp
    x %= M

    return x


# count = int(input("Введите число сравнений в системе: "))
# system = {}
# modules = []
# for i in range(1, count+1):
#     a, b, m = map(int, input(f"{i} Сравнение: ax=b(mod m) Введите a, b, m: ").split())
#     system[i] = [a, b, m]
#     modules.append(m)
#
# if are_coprime(modules):
#     print()
#     x = calculate_comparison_system(system)
#     print()
#     print("Система сравнений:")
#     for key in system:
#         print(f"{system[key][0]}x={system[key][1]}(mod {system[key][2]})")
#     print(f"Решение x = {x}")
# else:
#     print("Модули не взаимно простые")