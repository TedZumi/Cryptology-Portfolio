from Euler import euler_function


def reverse_element(a, m):
    euler_funk = euler_function(m)
    u = a ** (euler_funk - 1) % m
    return u


# a, m = map(int, input("Введите число и модуль: ").split())
# print(f"Обратный элемент {a} по модулю {m} = {reverse_element(a, m)}")