"""Realice un programa que lea por teclado 3 números, e muestre los valores ascendentemente."""

a = float(input("ingrese a"))
b = float(input("ingrese b"))
c = float(input("ingrese c"))

if a<b<c :
    print(a,b,c)
elif b<c<a :
    print(b,a,c)
elif c<a<b :
    print(c,a,b)
elif c<b<a :
    print(c,b,a)
elif a<c<b :
    print(a,c,b)
elif b<a<c :
    print (b,a,c)
else:
    print("existen valores iguales")
    