f = open('9_23268 (1).csv')

k = 1
for line in f:
    numbers = [int(x) for x in line.split(',')]
    cow = [numbers.count(x) for x in numbers]
    if cow.count(2) == 4 and cow.count(1) == 3:

        da = [x for x in numbers if numbers.count(x) > 1]
        net = [x for x in numbers if numbers.count(x) == 1]

        if sum(da) / len(da) < max(net):
            print(numbers, cow, da, net, sum(da) / len(da), max(net), k)
    k += 1
