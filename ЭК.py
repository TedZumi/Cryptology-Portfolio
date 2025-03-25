m = 13
for i in range(13):
    x = (i ** 3 + 8 * i + 1) % m
    y = i ** 2 % m
    print(f"i: {i}; x = {x}, y = {y}")

