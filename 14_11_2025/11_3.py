from math import *

K = 2783
n = 3_845_627

for N in range(1, 1000):
    i = ceil(log2(N))
    I = ceil(K * i / 8)
    In = I * n
    if In >= 11 * 1024 * 1024 * 1024:
        print(N)
