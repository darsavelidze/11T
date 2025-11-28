cache = [-1] * 16000

def f(n):
    return 2 * (g(n - 3) + 8)


def g(n):
    if cache[n] != -1:
        return cache[n]
    if n < 10:
        return 2 * n
    else:
        return g(n - 2) + 1

for i in range(1, 16000):
    cache[i] = g(i)


print(f(15548))