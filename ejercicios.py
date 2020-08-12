#imprimir Hola mundo por pantalla
print("Hola mundo")
#crear dos variables matemáticas, sumarlas y mostrar el resultado
x=1
y=2
print(x + y)
#crear un producto con valor de 100, agregarle el IVA y mostrar el resultado con y sin IVA
producto = 100
IVA = 0.21
precioIva= producto * IVA
print("el valor del producto es" + " $",producto)
print("con IVA incluído es" + " $",(producto + precioIva))
#de dos numeros saber cual es el mayor
x=11
y=12
if x > y:
    print ("x es mayor")
else:
    print ("y es mayor")
#Crear una variable, si está entre 0 y 10 mostrarlo
   #hay varias formas de hacerlo, independiente por cada variable
var = 9
varTwo= 12 
if var in range(0, 11):
    print ("var is between 0 and 10")
else: 
    print ("var is not between 0 and 10")

if varTwo in range(0, 11):
    print ("var is between 0 and 10")
else: 
    print ("var is not between 0 and 10")
   #a partir de una lista de variables
numone = 10
numtwo = 15
numthe = 6
numfou = 5
lista = [numone, numtwo, numthe, numfou]
for listadef in lista:  
    if listadef in range(0, 11):
        print ("number is in range between 0 and 10")
    else:
        print("number is not in range between 0 and 10")
#añadir tres mensajes al anterior (por cada una de las variables)
var = 9
varTwo= 12 
varthr= 50
if var in range(0, 11):
    print ("var is between 0 and 10")
elif var in range (11, 16):
    print("var is between 11 and 15")    
else: 
    print ("var is not between 0 and 15")

if varTwo in range(0, 11):
    print ("var is between 0 and 10")
elif varTwo in range (11, 16):
    print("var is between 11 and 15")
else: 
    print ("var is not between 0 and 10")

if varthr in range(0, 11):
    print ("var is between 0 and 10")
elif var in range (11, 16):
    print("var is between 11 and 15")    
else: 
    print ("var is not between 0 and 15")
   #por una lista de variables
numone = 10
numtwo = 15
numthe = 6
numfou = 5
numfiv = 50
lista = [numone, numtwo, numthe, numfou, numfiv]
for listadef in lista:  
    if listadef in range(0, 11):
        print ("number is between 0 and 10")
    elif listadef in range(11, 16):
        print ("number is between 11 and 15")
    else:
        print("number is not between 0 and 10")
#mostrar con un while numeros del 1 al 100
count = 0
while count <= 100:
    print(count)
    count = count + 1
#mostrar con un for los num del 1 al 10
for bignum in range(1, 11):
    print(bignum)
#mostrar los caracteres de la cadena "hola mundo"
for letter in "hola mundo":
    print(letter)
#mostrar numeros pares en un rango del 1 al 100
       #1ra forma
for parnum in range(1, 101):
    if ((parnum%2) == 0 ):
        print(parnum)

       #2da forma
for parnum in range(2, 101, 2):
    print(parnum)
#generar un rango de 0 a 10(con tupla)
rango= tuple(range(1,11))
print(rango)
#generar un rango de 0 a 10(con lista)
rango= list(range(1,11))
print(rango)
#generar uun numero entre 5 y 10
rango= list(range(5, 10))
print(rango)
#generar rango de 10 a 0
rango= list(range(10, 0, -1))
print(rango)
#generar un rango de 0 a 10 y de 15 a 20 incluyendo el 10 y el 20
rango= list(range(0,11))
rango2= list(range(15, 20))
print(rango + rango2)
#generar un rango desde 0 hasta la longitud de la cadena "hola mundo"
rango= list(range(0,len("hola mundo")))
print(rango)
#Pide dos cadenas por teclado, muestra ambas cadenas con un espacio entre ellas 
#y con los 2 primeros caracteres intercambiados.
cadena1 = input("primera cadena: ")
cadena2 = input("segunda cadena: ")
 
print( cadena2[:2] + cadena1[2:] + " " + cadena1[:2] + cadena2[2:] )
#esto de arriba quiere decir

#de la cadena2 agarra los 2 primeros caracteres([:2]) 
#y se lo suma a la cadena1 quien no tiene sus dos primeros caracteres([2:])

#se les suma un espacio en el medio

#de la cadena1 agarra los 2 primeros caracteres([:2])
#y se lo suma a la cadena2 quien no tiene sus dos primeros caracteres([2:])

#mostrar una palabra e insicar si es un palindromo o no(palabra que se lee derecha y de revés)
palabra = input("escribe una palabra: ")
 
palabra_al_reves = palabra[::-1] #esos simbolos ([::-1]) recorren los caracteres del reves
 
print(palabra_al_reves)
 
if( palabra == palabra_al_reves ):
    print("Es palindromo")
else:
    print("No es palindromo")



  



