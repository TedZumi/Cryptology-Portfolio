from primitive_root import calculate_primitive_root
from comparison import calculate_comparison
from Euler import euler_function


def calculate_ind(n, m):
    a = calculate_primitive_root(m)
    euler_f = euler_function(m)
    table_ind = {}
    for i in range(euler_f):
        b = a ** i % m
        table_ind[b] = i
    # print(table_ind)
    return table_ind[n]


# b, m = map(int, input("Введите число b и модуль m: ").split())
# ind = calculate_ind(b, m)
# print(f"m = {m}, ind({b}) = {ind}")
