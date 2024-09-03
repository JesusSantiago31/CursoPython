#else siempre conserva el ultimo valor de la literal
for i in range(5):
    print(i)
else:
    print("else:", i)

i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)

