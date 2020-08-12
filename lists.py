variable = ["elementodelistauno", "elementodelistados", "elementodelista3"]
variabledos = list(("elementodelistauan", "elementodelistatu", "elementodelistatri"))
print(variabledos)
print(variable)

# #lista basada en un rango (range)
# #lista que vaya del 1 al 101
# r = list(range(1, 101))
# print(r)

# #si utilizas el (dir) ves exactamente lo que se puede ejecutar de una lista
# print(dir(variabledos))

# #para obtener la longitud o cantidad de elementos en la lista
# print(len(variabledos))

# #para obtener el elemento en posicion 
# print(variabledos[-2])

# #ver si un elemento se encuentra en la lista
# print("elementodelistauan" in variabledos)
# print("green" in variabledos)

# #si deseo cambiar un elemento
# variabledos[1] = "yellow"
# print(variabledos)
# #esta es la variabilidad que tienen las listas, se pueden cambiar su contenido

# #si deseo añadir UN elemento
# variabledos.append("violet")
# print(variabledos)

# #si deseo agregar más de un elemento
#   #ejemplo: variabledos.append(("mio","tuyo"))
# print(variabledos)
# #aparece una tupla en la consola, para que no aparezca una tupla se debe de hacer de la siguiente manera
# #en vez de usar el APPEND se utiliza EXTEND
# variabledos.extend(("you", "me", "him"))
# print(variabledos)

# #podemos agregar un elemento en una posicion dada
# variabledos.insert(1, "for")
# print(variabledos)

# #para agregarlo justo a lo ultimo de la lista
# variabledos.insert(len(variabledos), "mio")
# print(variabledos)

# #para quitar un elemento
# variabledos.pop()
# print(variabledos)

# #para quitar más de un elemento
# variabledos.pop()
# variabledos.pop()
# print(variabledos)

# #si quiero basarme en un indice
# variabledos.pop(1)
# print(variabledos)

# #para quitar un elemento especifico
# variabledos.remove("yellow")
# print(variabledos)

# #para ordenar alfabeticamente SORT
# variabledos.sort()
# print(variabledos)


# #para ordenarlos a la inversa del alfabeto
# variabledos.sort(reverse = True)
# print(variabledos)

# #si quiero un indice de un elemento
# print(variabledos.index("elementodelistatri"))

# #si quiero saber cuantas veces existe el elemento
# print(variabledos.count("violet"))



