# print()
# dir()
# type()

def hello(name = " Person"):
    print("Hello" + name)
hello(" joe")
hello(" Martín")
hello()

# Funciones para matematicas
def suma(numberOne, numberTwo):
    return numberOne + numberTwo
print(suma(1, 3))
print(suma(2, 1000))

# lambda sirve para escribir el codigo en la misma linea y hacerlo más legible
add= lambda numberOne, numberTwo: numberOne + numberTwo
print(add(10, 30))


        
    
