 x = 1
y = 0
 
z = ((x == y) and (x == y)) or not(x == y)
print(not(z)) 
# = False
x = 4
y = 1

a = x & y
b = x | y
c = ~x  # ¡difícil!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)
# = 0 5 -5 1 1 16
