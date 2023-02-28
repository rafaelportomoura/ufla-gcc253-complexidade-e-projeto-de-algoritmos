preco = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# comprimento  1  2  3  4   5   6   7   8   9  10

haste = 10  # int(input("haste: "))

r = -1000  # infinito
m = [r for i in range(0, haste)]


def max(a, b):
    return a if a > b else b


for i in range(0, haste):
    r = m[i]
    for j in range(0, i):
        r = max(r, m[j] + m[i - j - 1])
    m[i] = max(r, preco[i])

print(m)
print(m[haste - 1])
