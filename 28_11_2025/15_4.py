for A in range(1, 100):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            F = (2 * x + y != 110) or (x < y) or (A < x)
            if F == 0:
                flag = False
    if flag:
        print(A)
