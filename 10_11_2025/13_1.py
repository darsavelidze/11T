ip = '192.168.1.206'
a = bin(192)[2:]
b = bin(50)[2:]
c = bin(1)[2:]
d = bin(206)[2:]
print(a.zfill(8), b.zfill(8), c.zfill(8), d.zfill(8))

mask = '255.255.255.255'
a = bin(255)[2:]
b = bin(255)[2:]
c = bin(255)[2:]
d = bin(224)[2:]
print(a.zfill(8), b.zfill(8), c.zfill(8), d.zfill(8))

a = bin(192)[2:]
b = bin(50)[2:]
c = bin(1)[2:]
d = bin(192)[2:]
print(a.zfill(8), b.zfill(8), c.zfill(8), d.zfill(8))


# 11000000 00110010 00000001 11011111