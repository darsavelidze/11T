from itertools import product
s = 'АЕКНОТ'
k = 1
for x in product(s, repeat=7):
    word = ''.join(x)
    if (word.count('К') == 2 and word.count('О') == 2 and word.count('Т') == 1
            and word.count('Е') == 1 and word.count('Н') == 1):
        if k % 2 == 1:
            print(k, word)
    k += 1

