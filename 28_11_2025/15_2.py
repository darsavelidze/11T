for A in range(1, 100):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            F = (x < A) and (y < 3 * A) or (2 * x + y > 128)
            if F == 0:
                flag = False
    if flag:
        print(A)
