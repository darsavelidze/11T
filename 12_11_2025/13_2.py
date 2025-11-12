print(bin(172)[2:].zfill(8))
print(bin(16)[2:].zfill(8))
print(bin(192)[2:].zfill(8))
print(bin(0)[2:].zfill(8))

k = 0
for i in range(0, 2**14):
    s = bin(i)[2:].zfill(14)
    if (7 + s.count('1')) % 5 != 0:
        k += 1

print(k)