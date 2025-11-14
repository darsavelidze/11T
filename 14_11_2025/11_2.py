from math import *

N = 10 + 17
i = ceil(log2(N)) # 5, bit
n = 7_564_230

for K in range(1, 10):
    I = ceil(K * i / 8)
    In = I * n
    if In > 31 * 1024 * 1024:
        print(K)