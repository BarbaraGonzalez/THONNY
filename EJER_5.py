"""Realice un programa que lea por teclado un texto, e indique la cantidad de vocales y consonantes"""

texto = input("ingrese texto")

contador_vocal = 0
contador_consonante = 0

cons_a = "a"
cons_e = "e"
cons_i = "i"
cons_o = "o"
cons_u = "u"

for i in texto:
    if (i==cons_a or i==cons_e or i==cons_i or i==cons_o or i==cons_u):
        contador_vocal += 1
    
    else:
        contador_consonante += 1
        
print(contador_vocal)
print(contador_consonante)



