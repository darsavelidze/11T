def f(ip):
    return '.'.join(bin(x)[2:].zfill(8) for x in map(int, ip.split('.')))


print(f('192.168.32.160'))
print(f('255.255.255.240'))


for i in range(0, 16):
    print(i, bin(i)[2:].zfill(4))