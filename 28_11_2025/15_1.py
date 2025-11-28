for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        F = (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))
        if F == 0:
            flag = False
    if flag:
        print(A)