def extended_gcd(a, b):
    x_1, x_2 = 1, 0
    y_1, y_2 = 0, 1
    i = 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        x_1, x_2 = x_2, x_1 - q * x_2
        y_1, y_2 = y_2, y_1 - q * y_2
        print(f"Шаг {i}, \nx_1 = {x_1}, x_2 = {x_2} \ny_1 = {y_1}, y_2 = {y_2}\nq = {q} \na = {a}, b = {b}")
        i += 1
    return a, x_1, y_1


a, b = map(int, input("Введите два числа через пробел: ").split())
d, u, v = extended_gcd(a, b)
print(f"({a}, {b}) = {d}\nЛинейное разложение a * ({u}) + b * ({v}) = {d}")