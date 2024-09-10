# Podemos intrcambiar los valores de algunas variables de la siguiente forma
variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary

# Usando las herramientas quen nos brinda python
variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1

# Ahora con listas
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

# Usando el ciclo for
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

