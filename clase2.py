# # MANEJO DE ARCHIVOS

# # ---------------------- 1 ---------------------- #
# # Primero indicamos el archivo que se va a utilizar y el modo de acceso
# Objeto = open('ejemplo.txt', 'r')

# # Ahora leemos el archivo
# var_1 = Objeto.read()
# print(var_1)

# # Cerramos el archivo
# Objeto.close()

# # ---------------------- 2 ---------------------- #
# # Abrir el archivo
# Objeto = open('ejemplo.txt', 'w')
# #Objeto = open('ejemplo.txt', 'r') # Esto da un error ya que el archivo esta abierto en modo escritura

# # Escribir en el archivo
# Objeto.write('Hola mundo')

# # Cerrar el archivo
# Objeto.close()

# # ---------------------- 3 ---------------------- #
# # Abrir el archivo
# Objeto = open('ejemplo.txt', 'r+')

# # Leer el archivo
# var_1 = Objeto.read()
# print(1,var_1)

# # Escribir en el archivo
# Objeto.write('\nHola, esto lo estoy mandando desde Python')

# # Cerrar el archivo
# Objeto.close()

# # Abrir el archivo
# Objeto = open('ejemplo.txt', 'r+')

# # Leer el archivo
# var_1 = Objeto.read()
# print(2,var_1)

# # Cerrar el archivo
# Objeto.close()


# # ---------------------- 4 ---------------------- #
# # Abrir el archivo
# Objeto = open('ejemplo.txt', 'w+')

# # Escribir en el archivo
# Objeto.write('Hola, esto lo estoy mandando desde Python')

# # Cerrar el archivo
# Objeto.close()


# # ---------------------- 5 ---------------------- #
# # Abrir el archivo
# Objeto = open('ejemplo.txt', 'a')

# # Leer el archivo
# var_1 = Objeto.read()
# print(var_1)

# # Escribir en el archivo
# Objeto.write('\nHola, esto lo estoy mandando desde Python')

# # Cerrar el archivo
# Objeto.close()


# LISTAS Y DICCIONARIOS

lista_1 = []
lista_2 = [15,16,17,18,19,20]

# Imprimir el numero 18
print(lista_2[3])

# Recorrer la lista
for i in lista_2:
    if i == 18:
        continue # Avanza a la siguiente iteracion
    print(i)

# Agregar 10 datos a lista 1
for i in range(10):
    lista_1.append(i)

# Imprimir lista 1
print(lista_1)


dict_1 = {}
dict_2 = {5:'Perro', 6:'Gato', 7:'Caballo'}

# Imprimir el valor de la llave 6
print(dict_2.keys())
print(dict_2.values())
print(dict_2[6])

# Imprimir el diccionario con for
for i in dict_2:
    print(i,dict_2[i])
