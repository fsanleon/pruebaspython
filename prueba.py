print("Hola Francisco")

""" 5- Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de 
una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""
print("Sumar 1,2,3,4 y la suma es:")
print(1 + 2 + 3 + 4)
print("Multiplicar 1,2,3,4 y la multiplicacion es:")
print(1 * 2 * 3 * 4)

print("_________________________________________________________________")


def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma


print(sumalista([1, 2, 3, 4]))

print("_________________________________________________________________")


def multiplista(listaNumeros):
    lamultip = 1
    for i in listaNumeros:
        lamultip = lamultip * i
    return lamultip
print(multiplista([1, 2, 3, 4]))

# Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
# También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)

myList = ["casa","solar", "tapa","tuberculosis","aladelta"]

def filtrarPalabras(myList,n):
    contador = 0
    listapalabras = []
    for palabra in myList:
        if palabra[0]== n or palabra.count(n) != 0:
            contador += 1
            listapalabras.append(palabra)
    return contador, listapalabras


n = input("escribir letra: ")
print(filtrarPalabras(myList,n))




