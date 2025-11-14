from math import *

i = ceil(log2(250 + 10))  # bit
K = 60

I = ceil(K * i / 8) # byte

n = 65_536
In = I * n / 1024 # Kb

print(In)