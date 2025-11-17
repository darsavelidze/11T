import string

x = 343 ** 515 - 6 * 49 ** 520 + 5 * 49 ** 510 - 3 * 7 ** 530 - 550

# 1, base < 10
s = ''

while x > 0:
    s = str(x % 7) + s
    x = x // 7

print(s.count('6'))

# 2, base < 10
x = 343 ** 515 - 6 * 49 ** 520 + 5 * 49 ** 510 - 3 * 7 ** 530 - 550

s = ''

k = 0
while x > 0:
    if x % 7 == 6:
        k += 1
    x = x // 7

print(k)


# 3, base > 10 and base < 36
x = 343 ** 515 - 6 * 49 ** 520 + 5 * 49 ** 510 - 3 * 7 ** 530 - 550

alf = '0123456789' + string.ascii_uppercase
s = ''

while x > 0:
    s = alf[x % 7] + s
    x = x // 7

print(s.count('6'))
