N = 1535
a = 4606
c = 711

sequence = []
x_i_1 = int(input("Введите стартовое значение x: "))
sequence.append(x_i_1)
for i in range(100):
    x_i = (a * x_i_1 + c) % N
    sequence.append(x_i)
    x_i_1 = x_i

# Вывод последовательности по 10 элементов в строке
elements_per_row = 10
for i in range(0, len(sequence), elements_per_row):
    row_elements = sequence[i:i + elements_per_row]
    print(*row_elements)

