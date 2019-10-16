def conversion_binaria(x):
    valor =""
    while x!=0:
        y=x//2
        z=x%2
        valor += str(z)
        x=y
    return valor 

N= int(input("ingrese N"))
RESULTADO = conversion_binaria(N)
print(RESULTADO)



