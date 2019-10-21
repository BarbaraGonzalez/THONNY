"""ejercicio 10
Realice un programa que determine si un número entero positivo es perfecto."""
def perfecto(x):
    suma = 0
    for i in range (1,x):
        suma= suma + i
    if suma == x:
        return True
    else:
        return False
    
n = int(input("ingrese un valor"))
 
if perfecto(n) ==True:
    print("es un número perfecto")
else:
    print("no es un número perfecto")

    