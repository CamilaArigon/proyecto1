myStr = "Camila Lucía"

#print(dir(myStr))

print("My name is " + myStr)
print(f"My name is {myStr}")
print("MY NAME IS {0}".format (myStr))
#esas son distintas formas de concadenar el string con otros valores

#print(dir(myStr)) este codigo se utiliza para ver las posibilidades que tenes para ejecutar con ese string

# print(myStr.upper())
# print(myStr.lower())
# print(myStr.swapcase())
# print(myStr.capitalize())
# print(myStr.replace("Lucía", "Arigón").upper()) #metodos encadenados
# print(myStr.startswith("Camila")) #mi string empieza con la palabra"Camila" 
# print(myStr.count("a")) #cuantas veces en el string está la letra "a"
# print(myStr.startswith("Lucía")) #mi string empieza con la palabra "Lucía"
#print(myStr.startswith("C")) #SE MANEJA CON CARACTERES ASI QUE CON LA "C" TAMBIEN DA TRUE
#print(myStr.split()) # separa las palabras del string
print(myStr.find("i")) #posicion de la letra (la cuenta comienza en cero)
print(len(myStr)) #longitud de el string (la cuenta comienza en cero)
print(myStr.index("l")) # muestra el indice de el caracter
print(myStr[2]) #muestra el caracter que se encuentra en el indice indicado entre corcheas
print(myStr[-4]) #si el num está en negativo, la cuenta comienza de atras hacia adelante
print(myStr.isnumeric())
print(myStr.isalpha())
print("my name is " + myStr)
