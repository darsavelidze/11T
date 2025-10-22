s = 'АЕКНОТ'
k = 1
for n1 in s:
    for n2 in s:
        for n3 in s:
            for n4 in s:
                for n5 in s:
                    for n6 in s:
                        for n7 in s:
                            word = n1 + n2 + n3 + n4 + n5 + n6 + n7
                            if (word.count('К') == 2 and word.count('О') == 2 and word.count('Т') == 1
                                    and word.count('Е') == 1 and word.count('Н') == 1):
                                if k % 2 == 1:
                                    print(k, word)
                            k += 1
