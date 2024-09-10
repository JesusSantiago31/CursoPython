# Suma de todos los elementos de una lista
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

# Haciendo mas eficiente el codigo
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

